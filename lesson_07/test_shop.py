from selenium import webdriver

from pages.ShopPage import ShopPage


def test_shop():
    driver = webdriver.Firefox()

    shop_page = ShopPage(driver)
    shop_page.open_shop()
    shop_page.authorization()
    shop_page.add_item()
    shop_page.shop_cart()
    shop_page.user_information()
    shop_page.total()
    shop_page.close_driver()
