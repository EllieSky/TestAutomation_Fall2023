from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from tests import BASE_URL

from selenium.webdriver.support import expected_conditions as EC


class DefineReportPage(BasePage):
    @property
    def PAGE_URL(self):
        return f'{BASE_URL}/core/definePredefinedReport'
    # PAGE_URL = f'{BASE_URL}/core/definePredefinedReport'

    def enter_report_name(self, report_name):
        self.wait.until(EC.presence_of_element_located(
            (By.ID, 'report_report_name'))).send_keys(report_name)

    def add_report_criteria(self, criteria):
        report_criteria_list = self.wait.until(EC.presence_of_element_located((By.ID, 'report_criteria_list')))
        Select(report_criteria_list).select_by_visible_text(criteria)
        self.browser.find_element(By.ID, 'btnAddConstraint').click()

    def set_selected_criteria_value__job_title(self, job_title):
        jt_select_elem = self.wait.until(EC.presence_of_element_located((By.ID, 'report_job_title')))
        Select(jt_select_elem).select_by_visible_text(job_title)

    def add_display_fields(self, field):
        report_display_field_list = self.wait.until(EC.presence_of_element_located((By.ID, 'report_display_field_list')))
        Select(report_display_field_list).select_by_visible_text(field)
        self.browser.find_element(By.ID, 'btnAddDisplayField').click()

    def save(self):
        self.browser.find_element(By.ID, 'btnSave').click()