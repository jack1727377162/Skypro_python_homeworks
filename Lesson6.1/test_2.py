from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_my_calculator():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver.maximize_window()
    waiter = WebDriverWait(driver, 100)

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    input_delay = driver.find_element(By.CSS_SELECTOR, "input#delay")
    input_delay.clear()
    input_delay.send_keys(45)

    driver.find_element(
        By.XPATH, "/html/body/main/div/div[4]/div/div/div[2]/span[1]").click()
    driver.find_element(
        By.XPATH, "/html/body/main/div/div[4]/div/div/div[2]/span[4]").click()
    driver.find_element(
        By.XPATH, "/html/body/main/div/div[4]/div/div/div[2]/span[2]").click()
    driver.find_element(
        By.XPATH, "/html/body/main/div/div[4]/div/div/div[2]/span[15]").click()

    m_example_result = driver.find_element(By.CSS_SELECTOR, "div.screen")

    waiter.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "div.screen"), "15"))

    assert m_example_result.text == "15"