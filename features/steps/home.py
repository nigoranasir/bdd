# home.py

from behave import *
from selenium.webdriver.common.by import By
from time import sleep

@given(u'user is logged in with bank-user role')
def step_impl(context):
    context.driver.get('https://demo.ebanq.com/log-in')
    context.driver.find_element(By.CSS_SELECTOR, '[type="email"]').send_keys('Demo-User')
    context.driver.find_element(By.CSS_SELECTOR, '[type="password"]').send_keys('Demo-Access1')
    context.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    sleep(5)

@given(u'user is logged in with bank-admin role')
def step_impl(context):
    context.driver.get('https://demo.ebanq.com/log-in')
    context.driver.find_element(By.CSS_SELECTOR, '[type="email"]').send_keys('Bank-Admin')
    context.driver.find_element(By.CSS_SELECTOR, '[type="password"]').send_keys('Demo-Access1')
    context.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    sleep(5)


@then(u'user can access "{side_menu}" side menu')
def step_impl(context, side_menu):
    displayed_side_menus = context.driver.find_elements(By.CSS_SELECTOR, 'label.aside__label')
    displayed_side_menus_names = [side_menu.text.lower() for side_menu in displayed_side_menus]
    assert side_menu.lower() in displayed_side_menus_names, f'{side_menu} not found in {displayed_side_menus_names}'


@then(u'user can not access "{side_menu}" side menu')
def step_impl(context, side_menu):
    displayed_side_menus = context.driver.find_elements(By.CSS_SELECTOR, 'label.aside__label')
    displayed_side_menus_names = [side_menu.text.lower() for side_menu in displayed_side_menus]
    assert side_menu.lower() not in displayed_side_menus_names, f'{side_menu} found in {displayed_side_menus_names}'