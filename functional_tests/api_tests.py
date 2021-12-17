from unittest import skip

from .base import APIFuncitonalTest


class TestShortURL(APIFuncitonalTest):

    def test_create_short_url_and_follow_it(self):
        # John has heard about new api for yet another URL shortener (yaus)
        # He sends POST request with his own URL
        # response contains new short link with yaus address in it
        url_to_be_shorten = {'url': self.url_to_be_shorten}
        response = self.client.post(path='/api/', data=url_to_be_shorten)
        shorten_url = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIn(self.django_test_server_domain, shorten_url)

        # He follow response URL to verify that it redirects to his URL
        response = self.client.get(path=f'/api/{shorten_url}', follow=True)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'] == self.url_to_be_shorten)

        # Satisfied, he goes back to sleep


class TestHumanReadableURL(APIFuncitonalTest):

    @skip
    def test_create_short_url_with_human_readable_name_and_follow_it(self):
        # John has heard about new api for yet another URL shortener (yaus)
        # He sends POST request with his own URL and new name for it
        # response contains new short link with yaus address in it
        url_to_be_shorten = {
            'url': self.url_to_be_shorten,
            'name': self.new_url_name,
        }
        response = self.client.post(path='/api/', data=url_to_be_shorten)
        shorten_url = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIn(self.django_test_server_domain, shorten_url)
        self.assertIn(self.new_url_name, shorten_url)

        # He follow response URL to verify that it redirects to his URL
        response = self.client.get(path=f'/api/{shorten_url}', follow=True)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'] == self.url_to_be_shorten)

        # Satisfied, he goes back to sleep
