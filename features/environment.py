# environment.py
from behave import *
from selenium import webdriver
from datetime import datetime
import os
from logs.logger import logger

def before_all(context):
    context.logger = logger

# steps that will run after each test case, tear down
def before_scenario(context, scenario):
    context.driver = webdriver.Firefox()
    context.logger.info("Starting browser Firefox")
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()

def after_scenario(context, scenario):
    timestamp = datetime.now().strftime("%m%d%y_%H%M%S")
    # context.driver.save_screenshot(fr'.\evidence\{scenario.name}_{timestamp}.png')
    # macOS and Windows compatible
    screenshot_path = os.path.join('evidence', f'{scenario.name}_{timestamp}.png')
    context.driver.save_screenshot(screenshot_path)
    context.driver.quit()
    context.logger.info("Closed the browser Firefox")