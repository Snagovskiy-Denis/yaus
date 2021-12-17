from django.test.testcases import LiveServerTestCase
from django.test.utils import override_settings
from rest_framework.test import APITestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class APIFuncitonalTest(APITestCase):
    django_test_server_domain = 'http://testserver'

    url_to_be_shorten = 'http://www.example.com'
    new_url_name = 'my-url'


@override_settings(DEBUG=True)
class UIFunctionalTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.selenium = WebDriver(executable_path='venv/geckodriver')
        cls.selenium.implicitly_wait(10)
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.selenium.quit()
        return super().tearDownClass()
