from behave import *

@when('we search for the logo')
def step_impl(context):   
   context.logo = context.browser.find_element_by_id("hplogo")
   

@then('logo is present!')
def step_impl(context):
   assert context.logo

