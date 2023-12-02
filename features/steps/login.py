# login.py
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@given(u'User is on login page')
def step_impl(context):
    url = context.config.userdata.get('url_qa')
    context.driver.get(url)
    context.logger.info(f'Navigated to login page {url}')


@when(u'User enters valid username')
def step_impl(context):
    username = context.config.userdata.get('customer_username')
    context.driver.find_element(By.CSS_SELECTOR, '[type="email"]').send_keys(username)
    context.logger.info(f'Entered valid username {username}')


@when(u'User enters valid password')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '[type="password"]').send_keys('Demo-Access1')
    context.logger.info('Entered valid password')


@when(u'User click on login button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    context.logger.info('Clicked on Login button')


@when(u'User enters username "{username}"')
def step_impl(context, username):
    if username == 'blank': username = ''
    context.driver.find_element(By.CSS_SELECTOR, '[type="email"]').send_keys(username)


@when(u'User enters password "{password}"')
def step_impl(context, password):
    if password == 'blank': password = ''
    context.driver.find_element(By.CSS_SELECTOR, '[type="password"]').send_keys(password)