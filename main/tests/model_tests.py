from unittest.mock import patch
from django.test import TestCase

from main.models import URL


class URLTest(TestCase):

    def test_save_with_valid_user_defined_short_name_saves_URL(self):
        URL.objects.create(full='http://www.example.com', short='example')
        try:
            URL.objects.get(short='example')
        except URL.DoesNotExist:
            self.fail('URL is saved with invalid SlugField value!')

    @patch('main.models.convert_10_to_62', return_value='a')
    @patch('main.models.ALLOWED_HOSTS', ['127.0.0.1'])
    def test_save_without_short_name_call_default_func(self, mock_converter):
        url = URL.objects.create(full='http://www.example.com')
        self.assertEqual(url.short, 'http://127.0.0.1/a')
        mock_converter.assert_called_with(number_10_radix=url.id)

    @patch('main.models.convert_10_to_62', return_value='a')
    def test_save_does_not_call_default_func_if_short_is_given(self, mock):
        URL.objects.create(full='http://www.example.com', short='example')
        mock.assert_not_called()
