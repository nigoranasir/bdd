from behave import *
from selenium.webdriver.common.by import By
from time import sleep
from random import randint, choice
import os

@when(u'User clicks on Accounts side menu')
def step_impl(context):
    sleep(5)
    context.driver.find_element(By.XPATH, f"//label[text()='Accounts']").click()


@when(u'User randomly click on any transaction')
def step_impl(context):
    transaction_ids = context.driver.find_elements(By.CSS_SELECTOR, '[title="ID"]')
    # random_index = randint(0, len(transaction_ids)-1)
    # id = transaction_ids[random_index]
    id = choice(transaction_ids)
    id.click()


@then(u'Transaction details displayed')
def step_impl(context):
    sleep(5)
    assert 'Transaction Details' in context.driver.page_source


@when(u'User clicks on account number dropdown')
def step_impl(context):
    context.driver.find_element(By.XPATH, f"//span[text()='Account number']").click()


@when(u'User clicks on any savings account option')
def step_impl(context):
    context.driver.find_element(By.XPATH, f"//span[text()=' Savings ']").click()


@then(u'Savings account details are displayed')
def step_impl(context):
    sleep(5)
    assert 'Savings' in context.driver.page_source

@when(u'User clicks on export icon')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, '[title="Export CSV"]').click()
    sleep(10)

@then(u'list of transactions are exported as csv file')
def step_impl(context):
    # path to downloads folder
    downloads_folder = os.path.expanduser('~/Downloads') # windows, mac compatibile
    # get names of all files in downloads folder
    files_in_downloads = os.listdir(downloads_folder)
    matching_files = [file for file in files_in_downloads if file.startswith('EBANQ Accounts')]
    assert len(matching_files) > 0