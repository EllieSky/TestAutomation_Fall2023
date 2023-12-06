from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
# comment 

def get_browser(browser_type: str):
    if browser_type.lower() == 'chrome':
        return webdriver.Chrome(
            service=Service(
                executable_path=ChromeDriverManager().install()))
    elif browser_type.lower() == 'firefox':
        return webdriver.Firefox(
            service=Service(
                executable_path=GeckoDriverManager().install()))
    else:
        raise ValueError(f'The browser type {browser_type} is not supported.')