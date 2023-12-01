import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestFramesAndWindows(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(
            service=Service(
                executable_path=ChromeDriverManager().install()))

    def tearDown(self):
        self.browser.quit()

    def test_within_frame(self):
        browser = self.browser
        browser.get('https://demoqa.com/frames')
        self.assertEqual(
            'Frames',
            browser.find_element(By.CLASS_NAME, 'main-header').text
        )

        iframe = browser.find_element(By.ID, 'frame1')
        browser.switch_to.frame(iframe)

        frame_text = browser.find_element(By.ID, 'sampleHeading').text

        self.assertEqual('This is a sample page', frame_text)

        browser.switch_to.default_content()

        browser.switch_to.frame(browser.find_element(By.ID, 'frame2'))
        frame2_text = browser.find_element(By.ID, 'sampleHeading').text

        self.assertEqual('This is a sample page', frame2_text)

    def test_nested_frames(self):
        expected_text = 'Child Iframe'

        browser = self.browser
        browser.get('https://demoqa.com/nestedframes')

        self.assertEqual(
            'Nested Frames',
            browser.find_element(By.CLASS_NAME, 'main-header').text
        )

        parent_frame = browser.find_element(By.ID, 'frame1')
        browser.switch_to.frame(parent_frame)

        child_frame = browser.find_element(By.TAG_NAME, 'iframe')
        browser.switch_to.frame(child_frame)

        self.assertEqual(expected_text, browser.find_element(By.XPATH, '//body/p').text)

        # browser.switch_to.parent_frame()   # to get back to parent frame
        # browser.switch_to.default_content()   # to get fully back out

    def test_other_page(self):
        browser = self.browser
        browser.get('https://demoqa.com/browser-windows')

        browser.find_element(By.ID, 'windowButton').click()

        open_windows = browser.window_handles
        browser.switch_to.window(open_windows[-1])

        window_url = browser.current_url
        self.assertIn('/sample', window_url)

        self.assertEqual(
            'This is a sample page',
            browser.find_element(By.ID, 'sampleHeading').text
        )

        browser.switch_to.window(open_windows[0])
        self.assertEqual(
            'Browser Windows',
            browser.find_element(By.CLASS_NAME, 'main-header').text
        )



if __name__ == '__main__':
    unittest.main()
