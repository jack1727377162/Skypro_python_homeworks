from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:

    def __init__(self, driver):
        self.driver = driver
        self.driver. get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def set_delay(self, delay):
        input_delay = self.driver.find_element(By.CSS_SELECTOR, "input#delay")
        input_delay.clear()
        input_delay.send_keys(delay)

    def input_text(self, keys_calculator):
        for val in keys_calculator:
            self.driver.find_element(
                By.XPATH, f'//span[text()="{val}"]').click()

    def wait_result(self, delay, result):
        waiter = WebDriverWait(self.driver, delay + 1)
        waiter.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '.screen'), str(result)))

    def result_text(self):
        result = self.driver.find_element(By.CSS_SELECTOR, '.screen')
        return result.text
