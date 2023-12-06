from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from tests import BASE_URL, DEFAULT_WAIT


class BasePage:
    PAGE_URL = f'{BASE_URL}'
    PAGE_HEADER = ''

    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.wait = WebDriverWait(browser, DEFAULT_WAIT)

    def goto_page(self):
        self.browser.get(self.PAGE_URL)