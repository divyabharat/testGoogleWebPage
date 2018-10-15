from behave import *

@when('we search for the search text field')
def step_impl(context):
   context.searchField = context.browser.find_element_by_name("q")
   

@then('search text field is present!')
def step_impl(context):
   assert context.searchField
   
