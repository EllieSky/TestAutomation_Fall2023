from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from tests import BASE_URL


class EmployeeReportPage(BasePage):
    PAGE_URL = f'{BASE_URL}/core/viewDefinedPredefinedReports'

    def click_add(self):
        self.browser.find_element(By.ID, 'btnAdd').click()


    def is_report_present(self, report_name):
        report_locator = f'//td[text() = "{report_name}"]'
        return self.wait.until(EC.presence_of_element_located((By.XPATH, report_locator)),
                        'The expected report name did not appear in the table within alloted time')