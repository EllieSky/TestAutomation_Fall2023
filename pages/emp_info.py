from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from fixtures.base_fixture import HRMFixture
from tests import BASE_URL, DEFAULT_WAIT

class EmployeeInfo:

    TABLE_HEADERS = ['Id', 'First (& Middle) Name',	'Last Name', 'Job Title', 'Employment Status', 'Sub Unit', 'Supervisor']

    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.wait = WebDriverWait(browser, DEFAULT_WAIT)

    def get_table_data(self, column_number, row_number):
        locator = f'//tr[{row_number}]/td[{column_number}]'
        return self.browser.find_element(By.XPATH, locator).text

    def click_table_header(self, table_header):
        if table_header not in self.TABLE_HEADERS:
            raise ValueError(f'Table header {table_header} is not a valid header')
        locator = f'//th/a[text()={table_header}]'
        self.browser.find_element(By.ID, locator).click()
