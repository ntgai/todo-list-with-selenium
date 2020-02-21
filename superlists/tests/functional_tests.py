import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Safari()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_starting_a_new_todo_list(self):
        self.browser.get('http://localhost:8000')

        self.assertIn("To-Do", self.browser.title)
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('To-Do', header.text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        inputbox.send_keys("Buy peacock feathers")
        # time.sleep(2)
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertIn(
            "1: Buy peacock feathers",
            [row.text for row in rows]
        )

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock featers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(
            "2: Use peacock feathers to make a fly",
            [row.text for row in rows]
        )
        self.assertIn(
            "1: Buy peacock feathers",
            [row.text for row in rows]
        )

        self.fail('Finish the test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
