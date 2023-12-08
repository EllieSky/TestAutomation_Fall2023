from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests import BASE_URL


class EmployeeReportPage(BasePage):
    PAGE_URL = f'{BASE_URL}/core/viewDefinedPredefinedReports/reportGroup/3/reportType/PIM_DEFINED'

    def click_add(self):
        self.browser.find_element(By.ID, 'btnAdd').click()

