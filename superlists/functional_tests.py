# import selenium, a test automator for web applications
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element_by_tag_name('h1')
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do list right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a To-Do item')

        # She types "Buy peacock feathers" into the textbox (Edith's hobby is tying flying fish lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates and now the page lists
        # '1: Buy peacock feathers" as an item on the to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # There's still a textbox inviting her to add another item. She enters "Use Peacock feathers to make a fly"
        # Edith is very methodical
        self.fail('Finish the test')

        # The page updates again and now shows both items on her list

        # Edith wonders whether the site will remember her list. Then she notices that the site has generated a unique URL for
        # her -- there is so: explanatory text to that effect

        # She visits the URL - her to-do list is still there.

        # Satisfied, she goes back to sleep

    def getMaxWindow(self):
        self.browser.maximize_window()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
