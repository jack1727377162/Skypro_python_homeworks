from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

user_name = driver.find_element(By.CSS_SELECTOR, "#user-name")
user_name.send_keys("standard_user")

password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("secret_sauce")

button = driver.find_element(By.CSS_SELECTOR, "#login-button")
button.click()

backpack = driver.find_element(
    By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
backpack.click()
sleep(2)

tshirt = driver.find_element(
    By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
tshirt.click()
sleep(2)

onesie = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
onesie.click()
sleep(2)

shop_cart = driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link")
shop_cart.click()
sleep(2)

checkout_button = driver.find_element(By.CSS_SELECTOR, "#checkout")
checkout_button.click()

first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
first_name.send_keys("Иван")
sleep(2)
last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
last_name.send_keys("Иванов")
sleep(2)
postal_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
postal_code.send_keys(350024)
sleep(2)
continue_button = driver.find_element(By.CSS_SELECTOR, "#continue")
continue_button.click()


total = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text

if total == "Total: $58.29":
    print("Passed")
else:
    print("Failure")

driver.quit()