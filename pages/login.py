from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from tests import BASE_URL, DEFAULT_WAIT


class LoginPage(BasePage):
    PAGE_URL = f'{BASE_URL}/auth/login'
    PAGE_HEADER = 'LOGIN Panel'

    def authenticate(self, username='admin', password='password'):
        self.browser.find_element(By.ID, 'txtUsername').send_keys(username)
        self.browser.find_element(By.ID, 'txtPassword').send_keys(password)
        self.browser.find_element(By.ID, 'btnLogin').click()
        # self.wait.until(EC.url_changes(f'{BASE_URL}/auth/login'))

    def get_message(self):
        return self.browser.find_element(By.ID, 'spanMessage').text