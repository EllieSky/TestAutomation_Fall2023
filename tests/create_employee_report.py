import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from fixtures.admin_login_fixture import AdminLoginFixture
from faker import Faker


class CreateEmployeeReport(AdminLoginFixture):
    def test_create_report_by_job_title(self):
        data = Faker()
        report_name = data.sentence()
        criteria = 'Job Title'

        self.emp_info_page.wait_for_page_to_load()
        self.emp_info_page.open_reports()

        self.emp_report.wait_for_page_to_load()
        self.emp_report.click_add()

        self.define_report.wait_for_page_to_load()
        self.define_report.enter_report_name(report_name)
        self.define_report.add_report_criteria(criteria)
        self.define_report.set_selected_criteria_value__job_title('QA Engineer')
        self.define_report.add_display_fields('Employee First Name')
        self.define_report.save()

        self.emp_report.wait_for_page_to_load()
        self.assertTrue(self.emp_report.is_report_present(report_name))





if __name__ == '__main__':
    unittest.main()
