import pytest
import allure
from selenium import webdriver
from urls import YandexScooterUrls
from pages.main_page import MainPage


@pytest.fixture(scope="function")
def driver():
    with allure.step('Создаем новый клиент браузера для совершения тестовых прогонов'):
        driver_instance = webdriver.Firefox()
        driver_instance.get(YandexScooterUrls.base_url)
        main_page = MainPage(driver_instance)

    yield driver_instance

    with allure.step('Закрываем созданный экземпляр браузерного клиента'):
        driver_instance.quit()

@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def order_page(driver):
    from pages.page_to_make_order import OrderPage
    return OrderPage(driver)


@pytest.fixture
def base_page(driver):
    from pages.base_page import BasePage
    return BasePage(driver)