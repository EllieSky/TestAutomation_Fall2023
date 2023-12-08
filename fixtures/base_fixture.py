import unittest

from selenium.webdriver.support.wait import WebDriverWait

from lib.browser import get_browser
from pages.define_report import DefineReportPage
from pages.emp_info import EmployeeInfo
from pages.emp_report import EmployeeReportPage
from pages.login import LoginPage
from tests import DOMAIN, DEFAULT_WAIT, BROWSER


class BaseFixture(unittest.TestCase):

    def setUp(self):
        self.browser = get_browser(BROWSER)
        self.wait = WebDriverWait(self.browser, DEFAULT_WAIT)

        self.login_page = LoginPage(self.browser)
        self.emp_info_page = EmployeeInfo(self.browser)
        self.emp_report = EmployeeReportPage(self.browser)
        self.define_report = DefineReportPage(self.browser)
        # self.add_emp_page = AddEmployyPage(self.browser)



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
