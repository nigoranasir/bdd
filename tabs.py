# import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# launch firefox
driver = webdriver.Firefox()
driver.maximize_window()

# go to web address
driver.get('http://the-internet.herokuapp.com/windows')

# click on the link
driver.find_element(By.CSS_SELECTOR, '.example > a').click()

sleep(2)

first_tab = driver.window_handles[0]
second_tab = driver.window_handles[1]

driver.switch_to.window(second_tab)
driver.close()

driver.switch_to.window(first_tab)
driver.close()