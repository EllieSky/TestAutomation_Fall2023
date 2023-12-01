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

    def tearDown(self):
        self.browser.quit()

    def test_valid_login(self):
        self.browser.get('http://hrm-online.portnov.com/')
        # find username field and enter data
        self.browser.find_element(By.ID, 'txtUsername').send_keys('admin')
        # find password field and enter data
        self.browser.find_element(By.ID, 'txtPassword').send_keys('password')
        # find login button and click
        self.browser.find_element(By.ID, 'btnLogin').click()
        # wait to login
        time.sleep(2)
        # check that login was valid
        greeting = self.browser.find_element(By.ID, 'welcome').text
        self.assertEqual('Welcome Admin', greeting)
        self.assertIn('/pim/viewEmployeeList', self.browser.current_url)
        # //div[@class='head']/h1   OR  .head>h1
        page_header = self.browser.find_element(By.XPATH, '//*[@id="employee-information"]/div[1]/h1').text
        self.assertEqual('Employee Information', page_header)


# //*[@id="resultTable"]/tbody/tr/td[3]/a
# #resultTable > tbody > tr:nth-child(1) > td:nth-child(3) > a


if __name__ == '__main__':
    unittest.main()
