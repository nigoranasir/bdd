# this file contains frequently used common functions such as 
# click on any tab by tab name
# click on any side menu by side menu name
# check any downloaded file with file name etc

from behave import *
from selenium.webdriver.common.by import By
from time import sleep
from random import randint
import os


@when(u'User clicks on "{side_menu}" side menu')
def step_impl(context, side_menu):
    sleep(5)
    context.driver.find_element(By.XPATH, f"//label[text()='{side_menu}']").click()
    sleep(5)


@when(u'the user clicks on tab "{tab}"')
def step_impl(context, tab):
    context.driver.find_element(By.XPATH, f"//span[text()='{tab}']").click()
    sleep(5)


@then(u'"{file_name}" is exported as csv file')
def step_impl(context, file_name):
    downloads_folder = os.path.expanduser('~/Downloads') # windows, mac compatibile
    files_in_downloads = os.listdir(downloads_folder)
    matching_files = [file for file in files_in_downloads if file.startswith(file_name)]
    assert len(matching_files) > 0


@then(u'new browser window opens with title "{window_title}"')
def step_impl(context, window_title):
    first_tab = context.driver.window_handles[0]
    second_tab = context.driver.window_handles[1]
    context.driver.switch_to.window(second_tab)
    assert window_title.lower() in context.driver.title.lower()


@when(u'User clicks "{button_text}" button')
def step_impl(context, button_text):
    sleep(5)
    context.driver.find_element(By.XPATH, f"//button[contains(text(), '{button_text}')]").click()
    sleep(5)


@then(u'"{text}" text is displayed')
def step_impl(context, text):
    timeout = 10
    found = False
    while timeout > 0:
        if text.lower() not in context.driver.page_source.lower():
            sleep(1)
            timeout -= 1
            context.logger.info(f'Waited for 1 second')
        else:
            found = True
            break
    assert found
    context.logger.info(f'Waited for {abs(timeout -10)}seconds')