from behave import *

@when('we search for the Search Button')
def step_impl(context):   
   context.searchButton = context.browser.find_element_by_name("btnK")


@then('Search Button field is present!')
def step_impl(context):
   assert context.searchButton
