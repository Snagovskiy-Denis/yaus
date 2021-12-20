from time import sleep
from selenium.webdriver.common.keys import Keys

from .base import UIFunctionalTest


class StandartUseCase(UIFunctionalTest):
    fixtures = ['urls']

    def test_create_new_short_url_and_follow_it(self):
        # Jane has heard about new new url shortener site
        # She goes to check out its homepage
        print(self.live_server_url)
        self.selenium.get(self.live_server_url)

        # She noticed the page title and header mention url shortener
        self.assertIn('yaus', self.selenium.title)
        header_text = self.selenium.find_element_by_tag_name('h1').text
        self.assertIn('Yet Another URL Shortener', header_text)

        # She is invited to enter a url straight away
        inputbox = self.selenium.find_element_by_id('id_full')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a URL to shorten...'
        )

        # She types 'www.example.com' into a text box
        inputbox.send_keys('http://www.example.com')

        # When she hits enter, the page lists
        # 'http://www.example.com -> is shortened to -> http://localhost/4'
        inputbox.send_keys(Keys.ENTER)
        sleep(3)
        link = self.selenium.find_element_by_tag_name('li')
        self.assertIn('http://127.0.0.1/4', link.text)

        # There is still a text box inviting her to add another item
        # Also Jane sees another text box below previous one
        # She enters 'https://www.python.org' in first field and 'py' in second one
        inputbox = self.selenium.find_element_by_id('id_full')
        inputbox.send_keys('https://www.python.org')
        inputbox = self.selenium.find_element_by_id('id_short')
        inputbox.send_keys('py')

        # New item appears below previous short item:
        # 'www.python.org -> is shortened to -> http://localhost/py'
        inputbox.send_keys(Keys.ENTER)
        sleep(3)
        link = self.selenium.find_element_by_tag_name('li')
        self.assertIn('http://127.0.0.1/py', link.text)

        # She follows short py url and it redirects her to www.python.org
        self.selenium.get(self.live_server_url + '/py')
        self.assertIn('Welcome to Python.org', self.selenium.title)

        # Satisfied, she goes to sleep
