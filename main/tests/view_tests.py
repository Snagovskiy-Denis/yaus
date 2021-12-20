from django.test import TestCase


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
