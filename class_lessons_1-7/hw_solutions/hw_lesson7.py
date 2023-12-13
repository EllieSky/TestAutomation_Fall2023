import unittest
from faker import Faker

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from fixtures.admin_login_fixture import AdminLoginFixture
from tests import PASSWORD


class AddEmployee(AdminLoginFixture):
    data = Faker()

    def test_add_amployee_with_username(self):
        first_name = self.data.first_name()
        last_name = self.data.last_name()

        self.wait.until(EC.presence_of_element_located((By.ID, 'btnAdd'))).click()
        self.wait.until(EC.url_contains('/pim/addEmployee'))

        self.wait.until(EC.presence_of_element_located((By.ID, 'firstName'))).send_keys(first_name)
        self.browser.find_element(By.ID, 'lastName').send_keys(last_name)
        emp_id = self.browser.find_element(By.ID, 'employeeId').get_attribute('value')
        username = f'{first_name}{last_name[0]}{emp_id}'
        self.browser.find_element(By.ID, 'chkLogin').click()

        self.wait.until(EC.visibility_of_element_located((By.ID, 'user_name'))).send_keys(username)
        self.browser.find_element(By.ID, 'user_password').send_keys(PASSWORD)
        self.browser.find_element(By.ID, 're_password').send_keys(PASSWORD)
        self.browser.find_element(By.ID, 'btnSave').click()

        self.wait.until(EC.url_contains('/pim/viewPersonalDetails/empNumber/'))
        self.browser.find_element(By.ID, 'welcome').click()
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Logout'))).click()

        self.wait.until(EC.url_contains('/auth/login'))

        self.browser.find_element(By.ID, 'txtUsername').send_keys(username)
        self.browser.find_element(By.ID, 'txtPassword').send_keys('password')
        self.browser.find_element(By.ID, 'btnLogin').click()

        greeting = self.wait.until(EC.presence_of_element_located((By.ID, 'welcome'))).text
        self.assertEqual(f'Welcome {first_name}', greeting)





if __name__ == '__main__':
    unittest.main()
