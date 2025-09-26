from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    edge_driver_path = r"C:\Users\User\edgedriver_win64\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    driver.implicitly_wait(4)

    first_name = driver.find_element(By.CSS_SELECTOR, "[name='first-name']")
    first_name.send_keys("Иван")
    first_name.click()

    last_name = driver.find_element(By.CSS_SELECTOR, "[name='last-name']")
    last_name.send_keys("Петров")
    last_name.click()

    address_input = driver.find_element(By.CSS_SELECTOR, "[name='address']")
    address_input.send_keys("Ленина, 55-3")
    address_input.click()

    email_address = driver.find_element(By.CSS_SELECTOR, "[name='e-mail']")
    email_address.send_keys("test@skypro.com")
    email_address.click()

    phone_number = driver.find_element(By.CSS_SELECTOR, "[name='phone']")
    phone_number.send_keys("+7985899998787")
    phone_number.click()

    city_name = driver.find_element(By.CSS_SELECTOR, "[name='city']")
    city_name.send_keys("Москва")
    city_name.click()

    country_name = driver.find_element(By.CSS_SELECTOR, "[name='country']")
    country_name.send_keys("Россия")
    country_name.click()

    job = driver.find_element(By.CSS_SELECTOR, "[name='job-position']")
    job.send_keys("QA")
    job.click()

    company_name = driver.find_element(By.CSS_SELECTOR, "[name='company']")
    company_name.send_keys("SkyPro")
    company_name.click()

    submit = driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary")
    submit.click()

    zip_code = driver.find_element(
        By.ID, "zip-code").value_of_css_property("background-color")

    waiter = WebDriverWait(driver, 30)
    waiter.until(EC.presence_of_element_located((By.ID, "zip-code")))

    assert zip_code == "rgba(248, 215, 218, 1)"

    fields = [
        "first-name",
        "last-name",
        "address",
        "city",
        "country",
        "e-mail",
        "phone",
        "job-position",
        "company"
    ]

    for field_id in fields:
        field_element = waiter.until(
            EC.visibility_of_element_located((By.ID, field_id)))
        border_color = field_element.value_of_css_property("border-color")
    assert border_color == "rgb(186, 219, 204)"

    driver.quit()
