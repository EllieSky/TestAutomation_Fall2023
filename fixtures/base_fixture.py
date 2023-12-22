import os
import unittest

from selenium.webdriver.support.wait import WebDriverWait

from lib.browser import get_browser
from menus.menu import Menu
from menus.user_menu import UserMenu
from pages.define_report import DefineReportPage
from pages.emp_info import EmployeeInfo
from pages.emp_report import EmployeeReportPage
from pages.login import LoginPage
from pages.page import Page
from tests import DOMAIN, DEFAULT_WAIT, BROWSER, TEST_RESULTS


class BaseFixture(unittest.TestCase):
    def setUp(self):
        self.browser = get_browser(BROWSER)
        self.wait = WebDriverWait(self.browser, DEFAULT_WAIT)

        self.page = Page(self.browser)

        self.login_page = LoginPage(self.browser)
        self.emp_info_page = EmployeeInfo(self.browser)
        self.emp_report = EmployeeReportPage(self.browser)
        self.define_report = DefineReportPage(self.browser)
        # self.add_emp_page = AddEmployyPage(self.browser)
        self.menu = Menu(self.browser)

    def tearDown(self):
        if ((hasattr(self._outcome, 'errors') and self._outcome.errors[1][1]) or
                (self._outcome.result.failures and self._outcome.result.failures[0][1])):
            if not os.path.exists(TEST_RESULTS):
                os.mkdir(TEST_RESULTS)

            pieces: list = self._outcome.result.current_test_id.split('.') \
                if hasattr(self._outcome.result, 'current_test_id') else self._outcome.result.nodeid.split('::')

            test_name = pieces.pop()

            folder_path = TEST_RESULTS
            for piece in pieces:
                folder_path = os.path.join(folder_path, piece)
                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)

            screenshot_path = os.path.join(folder_path, f'{test_name}.png')
            self.browser.save_screenshot(screenshot_path)

            page_src_path = os.path.join(folder_path, f'{test_name}.html')
            writable_file = open(page_src_path, 'w')
            writable_file.write(self.browser.page_source)
            writable_file.close()

        self.browser.quit()

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


class HRMFixture(BaseFixture):
    def setUp(self):
        super().setUp()
        # self.browser.get(DOMAIN)
        self.login_page.goto_page()
