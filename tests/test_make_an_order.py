import pytest
import allure
from selenium import webdriver
from data import Data
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.page_to_make_order import OrderPage


class TestMakeAnOrder:
    @allure.title('Проверка позитивного пути заказа самоката через верхнюю кнопку')
    @allure.description('В рамках данного тестового прогона проверяется, что при вводе валидных данных через верхнюю кнопку - у пользователя есть возможность оформить заказ самоката')
    def test_complete_order_flow_via_top_button(self, main_page, order_page):
        with allure.step('Нажимаем на кнопку создания заявки на заказ вверху страницы в шапке сайте'):
            main_page.order_button_top_click()
        with allure.step('Заполнить первую страницу заказа самоката: имя, фамилия, адрес доставки, ближайшую станцию метро и номер телефона'):
            order_page.fill_first_page(Data.ORDER_1)
        with allure.step('Заполнить вторую страницу заказа самоката: Дату доставки, срок аренды, цвет самоката и комментарий курьеру'):
            order_page.fill_second_page(Data.ORDER_1)
        with allure.step('После заполнения формы - открывается модальное окно, в открывшемся окне - нажать кнопку "Да"'):
            order_page.confirm_order()
        with allure.step('При нажатии на кнопку - "Да" появляется сообщение об успешном создании заявки, появляется кнопка "Проверить статус"'):
            assert order_page.check_success_message(), "Сообщение об успешном заказе не появилось"

    @allure.title('Проверка позитивного пути заказа самоката через нижнюю кнопку')
    @allure.description('В рамках данного тестового прогона проверяется, что при вводе валидных данных через нижнюю кнопку - у пользователя есть возможность оформить заказ самоката')
    def test_complete_order_flow_via_bottom_button(self, main_page, order_page):
        with allure.step('Нажимаем на кнопку создания заявки на заказ внизу страницы'):
            main_page.scrolling_to_order_button_big_and_click()
        with allure.step('Заполнить первую страницу заказа самоката: имя, фамилия, адрес доставки, ближайшую станцию метро и номер телефона'):
            order_page.fill_first_page(Data.ORDER_2)
        with allure.step('Заполнить вторую страницу заказа самоката: Дату доставки, срок аренды, цвет самоката и комментарий курьеру'):
            order_page.fill_second_page(Data.ORDER_2)
        with allure.step('После заполнения формы - открывается модальное окно, в открывшемся окне - нажать кнопку "Да"'):
            order_page.confirm_order()
        with allure.step('При нажатии на кнопку - "Да" появляется сообщение об успешном создании заявки, появляется кнопка "Проверить статус"'):
            assert order_page.check_success_message(), "Сообщение об успешном заказе не появилось"

    @classmethod
    def teardown_class(cls):
        with allure.step('Закрываем созданный экземпляр браузерного клиента'):
            cls.driver.quit()