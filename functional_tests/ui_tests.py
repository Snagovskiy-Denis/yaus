from .base import UIFunctionalTest


class StandartUseCase(UIFunctionalTest):
    fixtures = ['urls']

    def test_create_new_short_url_and_follow_it(self):
        # Jane has heard about new new url shortener site
        # She goes to check out its homepage
        print(self.live_server_url)
        self.selenium.get(self.live_server_url)

        # She noticed the page title and header mention url shortener
        self.assertIn('yaus' in self.selenium.title)

        # She is invited to enter a url straight away
        self.fail('unfinished test')

        # She types 'www.example.com' into a text box

        # When she hits enter, the page lists
        # 'www.example.com -> is shortened to -> http://localhost/4'

        # There is still a text box inviting her to add another item
        # Also Jane sees another text box below previous one
        # She enters 'www.python.org' in first field and 'py' in second one

        # New item appears below previous short item:
        # 'www.python.org -> is shortened to -> http://localhost/py'

        # She follows short py url and it redirects her to www.python.org

        # Satisfied, she goes to sleep
