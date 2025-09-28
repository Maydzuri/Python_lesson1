from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

text_field = driver.find_element(By.NAME, "username")
text_field.send_keys("tomsmith")
sleep(1)
text_field = driver.find_element(By.NAME, "password")
text_field.send_keys("SuperSecretPassword!")
sleep(1)
driver.find_element(By.CLASS_NAME, "radius").click()
sleep(3)
flash = driver.find_element(By.ID, "flash").text
print(flash)
driver.quit()
