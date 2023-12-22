from selenium.webdriver.common.by import By

from menus.base_menu import BaseMenu


class UserMenu(BaseMenu):
    link_welcome = (By.ID, 'welcome')
    link_logout = (By.XPATH, "//*[@id = 'welcome-menu']//a[text()='Logout']")

    def get_welcome_message(self):
        return self.get_text(self.link_welcome)

    def logout(self):
        self.click_elem(self.link_welcome)
        self.wait_for_elem_visible(self.link_logout).click()
