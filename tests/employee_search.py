import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from fixtures.admin_login_fixture import AdminLoginFixture


class EmpSearchTests(AdminLoginFixture):

    def test_search_by_name(self):
        search_word = 'Michael'
        time.sleep(1)
        self.emp_info_page.search_by_employee_name(search_word)
        time.sleep(2)
        self.assertEqual(search_word, self.emp_info_page.get_table_data(3, 1))


        list_of_first_name_elems = self.browser.find_elements(By.XPATH, '//tr/td[3]/a')

        for name_elem in list_of_first_name_elems:
            self.assertEqual(search_word, name_elem.text)

        self.menu.user.logout()



if __name__ == '__main__':
    unittest.main()
