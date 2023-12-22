from pages.define_report import DefineReportPage
from pages.emp_info import EmployeeInfo
from pages.emp_report import EmployeeReportPage
from pages.login import LoginPage


class Page:
    def __init__(self, browser):
        self.login = LoginPage(browser)
        self.emp_info = EmployeeInfo(browser)
        self.emp_report = EmployeeReportPage(browser)
        self.define_report = DefineReportPage(browser)
        # self.add_emp_page = AddEmployeePage(browser)