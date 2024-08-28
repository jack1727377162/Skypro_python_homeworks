from selenium import webdriver
from autom_calc_page import Calculator
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_calculator():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    delay = 45
    result = 15
    keys_press = '7+8='

    calc = Calculator(driver)
    calc.set_delay(delay)
    calc.input_text(keys_press)
    calc.wait_result(delay, result)

    assert calc.result_text() == str(result)
