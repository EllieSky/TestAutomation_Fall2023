import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class LoginTests(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(
            service=Service(
                executable_path=ChromeDriverManager().install()))
        self.browser.get('http://hrm-online.portnov.com/')

    def tearDown(self):
        self.browser.quit()

    def test_search_by_name(self):
        search_word = 'Michael'
        self.browser.find_element(By.ID, 'txtUsername').send_keys('admin')
        self.browser.find_element(By.ID, 'txtPassword').send_keys('password')
        self.browser.find_element(By.ID, 'btnLogin').click()
        time.sleep(1)
        self.browser.find_element(By.ID, 'empsearch_employee_name_empName').send_keys(search_word)
        self.browser.find_element(By.ID, 'searchBtn').click()
        time.sleep(2)
        list_of_first_name_elems = self.browser.find_elements(By.XPATH, '//tr/td[3]/a')

        for name_elem in list_of_first_name_elems:
            self.assertEqual(search_word, name_elem.text)



if __name__ == '__main__':
    unittest.main()
