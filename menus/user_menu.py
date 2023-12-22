from selenium.webdriver.common.by import By

from menus.base_menu import BaseMenu


class UserMenu(BaseMenu):
    link_welcome = (By.ID, 'welcome')

    def get_welcome_message(self):
        return self.get_text(self.link_welcome)