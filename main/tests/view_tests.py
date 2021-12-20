from unittest.mock import patch
from django.test import TestCase

from main.forms import URLShortenerForm
from main.models import URL


class RedirectByShortURL(TestCase):
    fixtures = ['urls']

    def test_get_by_default_name_redirects(self):
        response = self.client.get('/1')
        self.assertRedirects(response,
                             'http://www.example.com/',
                             fetch_redirect_response=False)

    def test_get_by_user_defined_short_name_redirects(self):
        response = self.client.get('/wiki')
        self.assertRedirects(response,
                             'https://wiki.archlinux.org/',
                             fetch_redirect_response=False)

    def test_get_non_existing_url_returns_404(self):
        response = self.client.get('/error')
        self.assertEqual(response.status_code, 404)


@patch('main.models.ALLOWED_HOSTS', ['127.0.0.1'])
class HomePage(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'main/home.html')

    def test_home_page_uses_url_form(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], URLShortenerForm)

    def test_post_saves_new_item(self):
        data = {'full': 'https://github.com', 'short': 'go'}
        response = self.client.post('/', data=data)
        self.assertEqual(URL.objects.count(), 1)
        new_url = URL.objects.first()
        self.assertEqual(new_url.full, 'https://github.com')
        self.assertEqual(new_url.get_short(), 'http://127.0.0.1/go')

    def test_for_invalid_input_doesnt_save_but_shows_errors(self):
        response = self.client.post('/', data={'full': '1', 'short': ''})
        self.assertEqual(URL.objects.count(), 0)
        self.assertContains(response, 'errorlist')
        self.assertNotContains(response, 'is shortened to')

    @patch('main.views.messages.success')
    def test_success_post_shows_shortened_url(self, mock_messages):
        data = {'full': 'https://github.com', 'short': ''}
        response = self.client.post('/', data=data)
        mock_messages.assert_called_once()
