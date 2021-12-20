from unittest import skip
from unittest.mock import patch

from .base import APIFuncitonalTest


@patch('main.models.ALLOWED_HOSTS', ['127.0.0.1'])
class TestShortURL(APIFuncitonalTest):

    def test_create_short_url_and_follow_it(self):
        # John has heard about new api for yet another URL shortener (yaus)
        # He sends POST request with his own URL
        # response contains new short link with yaus address in it
        url_to_be_shorten = {'url': self.url_to_be_shorten}
        response = self.client.post(path='/api/', data=url_to_be_shorten)
        *schema_and_domain, shorten_url = response.json().split('/')

        self.assertEqual(response.status_code, 200)
        self.assertIn('127.0.0.1', schema_and_domain)

        # He follow response URL to verify that it redirects to his URL
        response = self.client.get(path=f'/{shorten_url}')

        self.assertRedirects(response,
                             'http://www.example.com',
                             fetch_redirect_response=False)

        # Satisfied, he goes back to sleep


@patch('main.models.ALLOWED_HOSTS', ['127.0.0.1'])
class TestHumanReadableURL(APIFuncitonalTest):

    def test_create_short_url_with_human_readable_name_and_follow_it(self):
        # John has heard about new api for yet another URL shortener (yaus)
        # He sends POST request with his own URL and new name for it
        # response contains new short link with yaus address in it
        url_to_be_shorten = {
            'url': self.url_to_be_shorten,
            'name': self.new_url_name,
        }
        response = self.client.post(path='/api/', data=url_to_be_shorten)
        *schema_and_domain, shorten_url = response.json().split('/')

        self.assertEqual(response.status_code, 200)
        self.assertIn('127.0.0.1', schema_and_domain)
        self.assertIn(self.new_url_name, shorten_url)

        # He follow response URL to verify that it redirects to his URL
        response = self.client.get(path=f'/{shorten_url}')

        self.assertRedirects(response,
                             'http://www.example.com',
                             fetch_redirect_response=False)

        # Satisfied, he goes back to sleep
