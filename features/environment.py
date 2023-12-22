from selenium.webdriver.support.wait import WebDriverWait

from lib.base_methods import BaseMethods
from lib.browser import get_browser
from menus.user_menu import UserMenu
from pages.page import Page
from tests import DOMAIN, BROWSER, DEFAULT_WAIT


def before_scenario(context, scenario):
    if "no-browser" in scenario.effective_tags:
        return

    context.url = DOMAIN
    browser = get_browser(BROWSER)

    context.browser = browser
    context.wait = WebDriverWait(browser, DEFAULT_WAIT)
    context.base_methods = BaseMethods(browser)
    context.page = Page(browser)
    context.user_menu = UserMenu(browser)
    browser.get(context.url)


def after_scenario(context, scenario):
    if "no-browser" in scenario.effective_tags:
        return

    context.browser.quit()


# def before_all / after_all
# def before_feature(context, feature) / after_feature
# def before_step(context, step) / after_step
# def before_tag(context, tag) / after_tag