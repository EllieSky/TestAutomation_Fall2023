import unittest
from selenium.webdriver.support import expected_conditions as EC

from fixtures.admin_login_fixture import AdminLoginFixture


class CreateEmployeeReport(AdminLoginFixture):
    def test_create_report_by_job_title(self):
        # waiting for URL to match employee info page url
        # ensure successful login
        self.wait.until(EC.url_to_be(self.emp_info_page.PAGE_URL))

        # emp_info_page : go to pim > reports
        self.emp_info_page.open_reports()

        # we are now on the emp report page
        self.wait.until(EC.url_to_be(self.emp_report.PAGE_URL))

        # emp_reports_page:  click add
        self.emp_report.click_add()

        # define_report_page: enter report name
        # TODO: auto generate using faker
        report_name = 'REPORT'
        self.define_report.enter_report_name(report_name)

        # define_report_page: choose report criteria
        criteria = 'Job Title'
        self.define_report.add_report_criteria(criteria)
        self.define_report.set_selected_criteria_value__job_title('QA Engineer')
        pass



        # define_report_page: choose fileds to display
        # define_report_page: save
        # emp_reports_page: ensure the report appears in the table



if __name__ == '__main__':
    unittest.main()
