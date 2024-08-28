from selenium import webdriver
from autom_shop_page import User_shop
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_cl_shop():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    cl_shop = User_shop(driver)
    cl_shop.user_auth("standard_user", "secret_sauce")
    cl_shop.get_info()
    cl_shop.add_data_card(
        "Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"
    )
    cl_shop.place_order("Иван", "Иванов", "125319")

    total = cl_shop.get_result_price()
    assert total == "Total: $58.29"
    cl_shop._driver.quit()
