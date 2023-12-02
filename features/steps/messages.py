from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@when(u'User clicks on Messages icon')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div.controls__messages').click()
    sleep(5)


@when(u'User clicks on new message button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div > button').click()
    sleep(5)


@when(u'User enters message subject')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '[type="text"]').send_keys('Test Subject')


@when(u'User enters message body')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '[formcontrolname="body"]').send_keys('Test Body')


@when(u'User clicks send message')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div > button').click()
    sleep(5)