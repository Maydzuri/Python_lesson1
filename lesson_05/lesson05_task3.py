from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

text_field = driver.find_element(By.TAG_NAME, "input")
text_field.send_keys("Sky")
sleep(1)
text_field.clear()
text_field.send_keys("Pro")
sleep(1)
driver.quit()
