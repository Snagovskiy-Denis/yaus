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
        url = response.json()
        expected_url = URL.objects.get(full='http://www.example.com').short
        self.assertEqual(expected_url, url)

    def test_post_with_name_returns_created_url(self):
        URL.objects.create(full='http://wiki.archlinux.org', short='wiki')
        response = self.client.post(path=self.url,
                                    data=self.url_to_shorten_with_name)
        *schema_and_domain, slug = response.json().split('/')
        expected_slug = URL.objects.get(full='http://www.example.com').short
        self.assertEqual(expected_slug, slug)


class FollowShortURL(APITestCase):
    pass
