from behave import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@given('Search Text Field is present')
def step_impl(context):
   context.element = context.browser.find_element_by_name("q")
   assert context.element

@when('we enter "True Fit" in the Search Text Field and click on Search Button')
def step_impl(context):
   context.element.clear()
   context.element.send_keys("True Fit")

   context.browser.wait = WebDriverWait(context.browser, 10)
   button = context.browser.wait.until(EC.element_to_be_clickable((By.NAME, "btnK")))
   button.click()
   

@then('the title is updated to "True Fit" and yields some results')
def step_impl(context):
   assert "True Fit" in context.browser.title
   results = context.browser.find_elements_by_class_name('rc')
   assert results
