from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from menus.base_menu import BaseMenu


class MainMenu(BaseMenu):
    admin_menu = (By.ID, 'menu_admin_viewAdminModule')
    user_manag = (By.ID, 'menu_admin_UserManagement')
    user_configuration = (By.ID, 'menu_admin_Configuration')
    localization_menu_item = (By.ID, 'menu_admin_localization')

    def __init__(self, browser):
        super().__init__(browser)
        self.actions = ActionChains(self.browser)

    def admin_config_localization(self):
        (self.actions
         .move_to_element(self.wait.until(EC.presence_of_element_located(self.admin_menu)))
         .move_to_element(self.wait.until(EC.presence_of_element_located(self.user_manag)))
         .move_to_element(self.wait.until(EC.presence_of_element_located(self.user_configuration)))
         .click(self.wait.until(EC.presence_of_element_located(self.localization_menu_item)))
         .perform())
        self.wait.until(EC.url_contains('/admin/localization'))