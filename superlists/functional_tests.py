# import selenium, a test automator for web applications
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    # run selenium using the chrome browser
    def setUp(self):
        self.browser = webdriver.Chrome(
            'C:/Users/Ec/Desktop/Python/Software Dev practices/tdd_avec_python/browser/chromedriver')

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard of a cool new online to-do app. She goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices that the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do list right away

        # She types "Buy peacock feathers" into the textbox (Edith's hobby is tying flying fish lures)

        # When she hits enter, the page updates and now the page lists
        # '1: Buy peacock feathers" as an item on the to-do list

        # There's still a textbox inviting her to add another item. She enters "Use Peacock feathers to make a fly"
        # Edith is very methodical

        # The page updates again and now shows both items on her list

        # Edith wonders whether the site will remember her list. Then she notices that the site has generated a unique URL for
        # her -- there is so: explanatory text to that effect

        # She visits the URL - her to-do list is still there.

        # Satisfied, she goes back to sleep

    def getMaxWindow(self):
        self.browser.maximize_window()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
