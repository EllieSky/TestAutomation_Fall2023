import unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from fixtures.admin_login_fixture import AdminLoginFixture
from fixtures.base_fixture import BaseFixture


class MenuActionsTests(AdminLoginFixture):
    def test_select_localization(self):
        admin_menu = (By.ID, 'menu_admin_viewAdminModule')
        user_manag = (By.ID, 'menu_admin_UserManagement')
        user_configuration = (By.ID, 'menu_admin_Configuration')
        localization_menu_item = (By.ID, 'menu_admin_localization')

        # self.wait.until(EC.presence_of_element_located(admin_menu)).click()
        # self.wait.until(EC.presence_of_element_located(user_configuration)).click()
        # self.wait.until(EC.presence_of_element_located(localization_menu_item)).click()


        actions = ActionChains(self.browser)
        # actions.move_to_element(self.wait.until(EC.presence_of_element_located(admin_menu)))
        # actions.move_to_element(self.wait.until(EC.presence_of_element_located(user_manag)))
        # actions.move_to_element(self.wait.until(EC.presence_of_element_located(user_configuration)))
        # actions.click(self.wait.until(EC.presence_of_element_located(localization_menu_item)))
        # actions.perform()


        # OR

        actions = ActionChains(self.browser)
        (actions
         .move_to_element(self.wait.until(EC.presence_of_element_located(admin_menu)))
         .move_to_element(self.wait.until(EC.presence_of_element_located(user_manag)))
         .move_to_element(self.wait.until(EC.presence_of_element_located(user_configuration)))
         .click(self.wait.until(EC.presence_of_element_located(localization_menu_item)))
         .perform())
        self.wait.until(EC.url_contains('/admin/localization'))


class DragAndDropExample(BaseFixture):
    def test_drag_and_drop(self):
        self.browser.get('https://demoqa.com/dragabble')
        actions = ActionChains(self.browser)
        actions.click_and_hold(self.browser.find_element(By.ID, 'dragBox'))
        actions.move_by_offset(100, 30).pause(2)
        actions.move_by_offset(50, -20).pause(1)
        actions.move_by_offset(-75, 10).pause(1)
        actions.release()
        actions.perform()

        actions.drag_and_drop_by_offset(self.browser.find_element(By.ID, 'dragBox'), -45, 30).perform()


if __name__ == '__main__':
    unittest.main()
