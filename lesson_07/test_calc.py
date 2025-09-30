from selenium import webdriver

from pages.CalcPage import CalcPage


def test_calc():
    driver = webdriver.Chrome()

    calc_page = CalcPage(driver)
    calc_page.open_calculator()
    calc_page.calculator_waits('45')
    calc_page.button_click()
    calc_page.check()
    calc_page.close_driver()
