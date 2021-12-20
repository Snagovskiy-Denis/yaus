from unittest.mock import patch

from rest_framework.test import APITestCase
from rest_framework import status

from main.models import URL


@patch('main.models.ALLOWED_HOSTS', ['127.0.0.1'])
class CreateShortURL(APITestCase):

    url = '/api/'
    url_to_shorten = {'url': 'http://www.example.com'}

    url_to_shorten_with_name = {
        'url': 'http://www.example.com',
        'name': 'short-name'
    }

    def test_post_returns_200_json(self):
        response = self.client.post(path=self.url, data=self.url_to_shorten)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_post_creates_new_url_in_database(self):
        self.client.post(path=self.url, data=self.url_to_shorten)
        if not URL.objects.first():
            self.fail('POST did not create new entity in database')

    def test_post_invalid_data_returns_erors(self):
        invalid_data = {'url': 'http://wo*two.com'}
        response = self.client.post(path=self.url, data=invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        error = response.json().get('full')
        self.assertEqual(error, ['Enter a valid URL.'])

    def test_post_invalid_data_do_not_save_url(self):
        invalid_data = {'url': 'http://wo*two.com'}
        self.client.post(path=self.url, data=invalid_data)
        self.assertEqual(URL.objects.count(), 0)

    def test_post_returns_created_url(self):
        URL.objects.create(full='http://archlinux.org', short='')
        response = self.client.post(path=self.url, data=self.url_to_shorten)
        expected_url = URL.objects.get(full='http://www.example.com')
        self.assertEqual(expected_url.get_short(), response.json())

    def test_post_with_name_returns_created_url(self):
        URL.objects.create(full='http://wiki.archlinux.org', short='wiki')
        response = self.client.post(path=self.url,
                                    data=self.url_to_shorten_with_name)
        self.assertEqual('http://127.0.0.1/short-name', response.json())

    def test_post_returns_error_if_short_name_already_exists(self):
        self.client.post(path=self.url, data=self.url_to_shorten_with_name)
        response = self.client.post(path=self.url,
                                    data=self.url_to_shorten_with_name)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        error = response.json().get('short')[0]
        self.assertEqual(error, 'url with this short already exists.')

    def test_user_defined_short_name_max_length_is_50(self):
        url_with_invalid_short_name = {
            'url': 'http://hacker.com',
            'name': 'spam' * 50
        }
        response = self.client.post(path=self.url,
                                    data=url_with_invalid_short_name)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        error = response.json().get('short')[0]
        self.assertIn('no more than 50 characters', error)

    def test_short_name_can_not_contain_unsafe_characters(self):
        url_with_invalid_short_name = {
            'url': 'http://hacker.com',
            'name': '<script>alert("Hacked!")</script>'
        }
        response = self.client.post(path=self.url,
                                    data=url_with_invalid_short_name)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        error = response.json().get('short')[0]
        self.assertIn('Enter a valid "slug"', error)


class FollowShortURL(APITestCase):
    pass
