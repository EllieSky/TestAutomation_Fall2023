from menus.main_menu import MainMenu
from menus.user_menu import UserMenu


class Menu:
    def __init__(self, browser):
        self.main = MainMenu(browser)
        self.user = UserMenu(browser)