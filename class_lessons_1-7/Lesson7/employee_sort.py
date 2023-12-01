import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class EmployeeSort(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(
            service=Service(
                executable_path=ChromeDriverManager().install()))
        self.browser.get('http://hrm-online.portnov.com/')

    def tearDown(self):
        self.browser.quit()

    def test_sort_by_name(self):
        self.browser.find_element(By.ID, 'txtUsername').send_keys('admin')
        self.browser.find_element(By.ID, 'txtPassword').send_keys('password')
        self.browser.find_element(By.ID, 'btnLogin').click()

        wait = WebDriverWait(self.browser, 10)

        # waiting for welcome message and asserting text
        self.assertEqual(
            'Welcome Admin',
            wait.until(expected_conditions.presence_of_element_located((By.ID, 'welcome'))).text
        )

        # waiting for url change
        wait.until(expected_conditions.url_contains('/pim/viewEmployeeList'))

        # waiting for the table header and clicking
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//th[3]/a'))).click()

        ### ALL OF THESE LOCATE THE SAME HEADER ELEMENT
        # self.browser.find_element(By.XPATH, '//th[3]/a')
        # self.browser.find_element(By.XPATH, "//a[text() = 'First (& Middle) Name']")
        ### This is replaced by wait command on line 40
        # self.browser.find_element(By.LINK_TEXT, 'First (& Middle) Name').click()

        wait.until(expected_conditions.url_contains('?sortField=firstMiddleName&sortOrder=ASC'))

        wait.until(expected_conditions.text_to_be_present_in_element_attribute(
            (By.XPATH, '//th[3]/a'), 'class', 'ASC')
        )

        name_elems = self.browser.find_elements(By.XPATH, '//tr/td[3]/a')

        previous_name = ''
        for name in name_elems:
            current_name = name.text
            self.assertLessEqual(previous_name, current_name)
            previous_name = current_name



if __name__ == '__main__':
    unittest.main()
