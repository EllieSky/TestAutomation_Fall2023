import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class MyFirstUITest(unittest.TestCase):
    def test_hello_google(self):
        browser = webdriver.Chrome(
            service=Service(
                executable_path=ChromeDriverManager().install()))
        browser.get('http://www.google.com')
        browser.find_element(By.NAME, 'q').send_keys('Hello')
        browser.find_element(By.NAME, 'q').submit()
        time.sleep(2)
        link = browser.find_element(By.CSS_SELECTOR, 'a>h3').text
        self.assertIn("hello", link.lower())

if __name__ == '__main__':
    unittest.main()
