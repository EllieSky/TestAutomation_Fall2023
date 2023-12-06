from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.base_fixture import HRMFixture
from tests import BASE_URL


class AdminLoginFixture(HRMFixture):
    def setUp(self):
        super().setUp()
        # self.browser.find_element(By.ID, 'txtUsername').send_keys('admin')
        # self.browser.find_element(By.ID, 'txtPassword').send_keys('password')
        # self.browser.find_element(By.ID, 'btnLogin').click()
        self.login_page.authenticate()



        self.wait.until(EC.url_changes(f'{BASE_URL}/auth/login'))


