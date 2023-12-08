from selenium.webdriver.support import expected_conditions as EC

from fixtures.base_fixture import HRMFixture
from tests import BASE_URL


class AdminLoginFixture(HRMFixture):
    def setUp(self):
        super().setUp()
        self.login_page.authenticate()
        self.wait.until(EC.url_changes(f'{BASE_URL}/auth/login'))


