from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from tests import BASE_URL, DEFAULT_WAIT


class EmployeeInfo(BasePage):
    PAGE_URL = f'{BASE_URL}/pim/viewEmployeeList'
    PAGE_HEADER = 'Employee Information'

    TABLE_HEADERS = [
        'Id',
        'First( & Middle) Name',
        'Last Name',
        'Job Title',
        'Employment Status',
        'Sub Unit',
        'Supervisor',
    ]

    btn_search = (By.ID, 'searchBtn')
    btn_reset = (By.ID, 'resetBtn')
    btn_add = (By.ID, 'btnAdd')

    select_job_title = (By.ID, 'empsearch_job_title')
    fld_emp_name = (By.ID, 'empsearch_employee_name_empName')

    def get_table_data(self, column_number, row_number):
        locator = f'//tr[{row_number}]/td[{column_number}]'
        return self.browser.find_element(By.XPATH, locator).text

    def click_table_header(self, table_header):
        if table_header not in self.TABLE_HEADERS:
            raise ValueError(f'Table header "{table_header}" is not a valid header value')
        locator = f'//th/a[text() = "{table_header}"]'
        self.browser.find_element(By.ID, locator).click()

    def reset_search_form(self):
        self.browser.find_element(*self.btn_reset).click()

    def search_by_job_title(self, job_title):
        select_elem = self.browser.find_element(*self.select_job_title)
        Select(select_elem).select_by_visible_text(job_title)

        self.browser.find_element(*self.btn_search).click()

    def search_by_employee_name(self, emp_name):
        self.browser.find_element(*self.fld_emp_name).send_keys(emp_name)
        self.browser.find_element(*self.btn_search).click()