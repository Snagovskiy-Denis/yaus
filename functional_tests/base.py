from django.test.testcases import LiveServerTestCase
from django.test.utils import override_settings
from rest_framework.test import APITestCase
from selenium.webdriver.firefox.webdriver import WebDriver


# @override_settings(ALLOWED_HOSTS=['127.0.0.1'])
class APIFuncitonalTest(APITestCase):
    url_to_be_shorten = 'http://www.example.com'
    new_url_name = 'my-url'


@override_settings(DEBUG=True)
class UIFunctionalTest(LiveServerTestCase):
    url_to_be_shorten = 'http://www.example.com'
    new_url_name = 'my-url'

    @classmethod
    def setUpClass(cls) -> None:
        cls.selenium = WebDriver(executable_path='venv/geckodriver')
        cls.selenium.implicitly_wait(10)
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.selenium.quit()
        return super().tearDownClass()
