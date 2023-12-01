import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from lib.browser import get_browser
from tests import DOMAIN, DEFAULT_WAIT, BROWSER


class BaseFixture(unittest.TestCase):

    def setUp(self):
        self.browser = get_browser(BROWSER)
        self.wait = WebDriverWait(self.browser, DEFAULT_WAIT)

    def tearDown(self):
        self.browser.quit()

    # def setUpClass(cls):
    #     pass
    #
    # def tearDownClass(cls):
    #     pass


class HRMFixture(BaseFixture):
    def setUp(self):
        super().setUp()
        self.browser.get(DOMAIN)
