from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

for x in range(1, 4):
    driver.get("http://uitestingplayground.com/dynamicid")
    driver.find_element(By.CSS_SELECTOR, "button.btn").click()
    sleep(5)

sleep(5)