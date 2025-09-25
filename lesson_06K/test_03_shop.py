from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/")

username_field = driver.find_element(By.ID, 'user-name')
password_field = driver.find_element(By.ID, 'password')
login_button = driver.find_element(By.ID, 'login-button')

username_field.send_keys('standard_user')
password_field.send_keys('secret_sauce')
login_button.click()

driver.implicitly_wait(10)

item_add_1 = driver.find_element(
    By.ID, 'add-to-cart-sauce-labs-backpack').click()
item_add_2 = driver.find_element(
    By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
item_add_3 = driver.find_element(
    By.ID, 'add-to-cart-sauce-labs-onesie').click()

driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

driver.find_element(By.ID, 'checkout').click()

first_name = driver.find_element(By.ID, 'first-name')
first_name.send_keys('Robert')

last_name = driver.find_element(By.ID, 'last-name')
last_name.send_keys('Gazizullin')

postal_code = driver.find_element(By.ID, 'postal-code')
postal_code.send_keys('663300')

driver.find_element(By.ID, 'continue').click()

total = driver.find_element(By.CLASS_NAME, 'summary_total_label').text
total_value = float(total.split('$')[1])
print(total)

assert total_value == 58.29

driver.quit()
