from behave import *
from selenium.webdriver.common.keys import Keys

@given('Search Text Field is there')
def step_impl(context): 
	context.element = context.browser.find_element_by_name("q")
	assert context.element.is_displayed()

@when('there is no text in the Search Text Field and Search Button is clicked')
def step_impl(context):
	context.element.clear()
	button = context.browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
	context.browser.execute_script("arguments[0].click();", button)

   

@then('no results are displayed')
def step_impl(context):
	assert context.browser.title=="Google"
	
