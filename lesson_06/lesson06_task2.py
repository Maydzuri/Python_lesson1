from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://uitestingplayground.com/textinput')

input = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input.send_keys('SkyPro')

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
txt = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

print(f'"{txt}"')

driver.quit
