from selenium import webdriver
from autom_data_page import Autom_data
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_auth_form():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    auth_page = Autom_data(driver)
    auth_page.person_data(
        "Иван",
        "Петров",
        "Ленина, 55-3",
        "",
        "Москва",
        "Россия",
        "test@skypro.com",
        "+7985899998787",
        "QA",
        "SkyPro",
    )
    auth_page.check_person_data()
    success_results, danger_results = auth_page.get_result()

    success_class = "alert-success"
    danger_class = "alert-danger"

    for i in success_results:
        assert success_class in i

    for k in danger_results:
        assert danger_class in k

    auth_page.driver.quit()
