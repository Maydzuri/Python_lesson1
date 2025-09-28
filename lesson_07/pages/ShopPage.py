from selenium.webdriver.common.by import By

driver = None


class ShopPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()

    def open_shop(self):
        url = "https://www.saucedemo.com/"
        self._driver.get(url)

    def authorization(self):
        self._driver.find_element(
            By.ID, 'user-name').send_keys('standard_user')
        self._driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self._driver.find_element(By.ID, 'login-button').click()
        self._driver.implicitly_wait(10)

    def add_item(self):
        self._driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(
            By.ID, 'add-to-cart-sauce-labs-onesie').click()

    def shop_cart(self):
        self._driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
        self._driver.find_element(By.ID, 'checkout').click()

    def user_information(self):
        self._driver.find_element(By.ID, 'first-name').send_keys('Robert')
        self._driver.find_element(By.ID, 'last-name').send_keys('Gazizullin')
        self._driver.find_element(By.ID, 'postal-code').send_keys('663300')
        self._driver.find_element(By.ID, 'continue').click()

    def total(self):
        total = self._driver.find_element(
            By.CLASS_NAME, 'summary_total_label').text
        total_value = float(total.split('$')[1])
        assert total_value == 58.29

    def close_driver(self):
        self._driver.quit()
