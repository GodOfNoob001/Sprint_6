from selenium import webdriver
from urls import YandexScooterUrls
from pages.base_page import BasePage
import allure
from urls import YandexScooterUrls
from conftest import base_page, main_page, driver

class TestPageTransfer:

    @classmethod
    def setup_class(cls):
        with allure.step('Создаем новый клиент браузера для совершения тестовых прогонов'):
            cls.driver = webdriver.Firefox()

    @allure.title('При нажатии на логотип "Самокат" на странице - происходит редирект на главную страницу Яндекс.Самокат')
    @allure.description('В рамках данного тестового прогона проверяется, что при нажатии на логотип "Самокат" на странице - происходит редирект на главную страницу Яндекс.Самокат вне зависимости от того, на какой странице был нажат логотип')
    def test_success_transfer_to_main_page_by_click_scooter_label(self, base_page, main_page):
        with allure.step('Нажимаем на кнопку "Заказать" для перехода на другую страницу'):
            main_page.order_button_top_click()
        base_page.wait_for_url_contains("/order")
        with allure.step('Нажимаем на логотип "Самокат" в шапке сайте'):
            main_page.scooter_logo_click()
        base_page.wait_for_url(YandexScooterUrls.base_url)
        with allure.step('При нажатии на логотип "Самокат" в шапке сайте - происходит редирект на главную страницу сервиса'):
            assert base_page.get_current_url() == YandexScooterUrls.base_url

    @allure.title('При нажатии на логотип "Яндекс" на главной странице - происходит редирект на страницу Дзен')
    @allure.description('В рамках данного тестового прогона проверяется, что при переходе к FAQ-блоку - вопросы отображаются, значения вопросов валидны')
    def test_success_transfer_to_dzen_page_by_click_yandex_label(self, base_page, main_page):
        with allure.step('Нажимаем на логотип "Яндекс" в шапке сайте'):
            main_page.yandex_logo_click()
        base_page.wait_for_new_window_and_switch()
        base_page.wait_for_url_contains("?yredirect=true")
        with allure.step('При нажатии на логотип "Яндекс" в шапке сайте - происходит редирект на главную страницу сервиса "Дзен"'):
            assert YandexScooterUrls.dzen_url == base_page.get_current_url()