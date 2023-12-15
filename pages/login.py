from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests import BASE_URL, ADMIN_USER, PASSWORD


class LoginPage(BasePage):
    @property
    def PAGE_URL(self):
        return f'{BASE_URL}/auth/login'

    # The property above replaces this variable
    # PAGE_URL = f'{BASE_URL}/auth/login'

    PAGE_HEADER = 'LOGIN Panel'

    def authenticate(self, username=ADMIN_USER, password=PASSWORD):
        self.browser.find_element(By.ID, 'txtUsername').send_keys(username)
        self.browser.find_element(By.ID, 'txtPassword').send_keys(password)
        self.browser.find_element(By.ID, 'btnLogin').click()
        # self.wait.until(EC.url_changes(f'{BASE_URL}/auth/login'))

    def get_message(self):
        return self.browser.find_element(By.ID, 'spanMessage').text