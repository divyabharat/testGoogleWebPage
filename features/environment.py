# -- FILE: features/environment.py
from behave import fixture, use_fixture
from selenium import webdriver

@fixture
def selenium_browser_chrome(context):
    pathToChromeDriver = '/Users/divyabharat/Downloads/chromedriver'
    context.browser = webdriver.Chrome(pathToChromeDriver)
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()

def before_all(context):
   use_fixture(selenium_browser_chrome, context)


def before_scenario(context, scenario):
    context.browser.get('http://www.google.com')
