from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = None


class CalcPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()

    def open_calculator(self):
        url = "https://bonigarcia.dev/selenium-webdriver-java/" \
            "slow-calculator.html"
        self._driver.get(url)

    def calculator_waits(self, seconds):
        waits = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        waits.clear()
        waits.send_keys(seconds)

    def button_click(self):
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="="]').click()
        waiter = WebDriverWait(self._driver, 52)
        waiter.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, 'div.screen'), '15'))

    def check(self):
        result = self._driver.find_element(
            By.CSS_SELECTOR, "div.screen").text
        print(result)
        assert "15" in result

    def close_driver(self):
        self._driver.quit()
