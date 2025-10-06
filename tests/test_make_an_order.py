import pytest
import allure
from selenium import webdriver
from data import Data
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.page_to_make_order import OrderPage


class TestMakeAnOrder:
    @classmethod
    def setup_class(cls):
        with allure.step('Создаем новый клиент браузера для совершения тестовых прогонов'):
            cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize("order_data,order_button", [
        (Data.ORDER_1, "top"),
        (Data.ORDER_2, "bottom")
    ])
    @allure.title('Проверка позитивного пути заказа самокатов в двух итерациях и с валидными данными')
    @allure.description('В рамках данного тестового прогона проверяется, что при вводе валидных данных - у пользователя есть возможность оформить заказ самоката')
    def test_complete_order_flow(self, order_data, order_button):
        with allure.step('Открываем сайт для дальнейшей работы с тестовым прогоном'):
            self.driver.get(YandexScooterUrls.base_url)
        if order_button == "top":
            with allure.step('Нажимаем на кнопку создания заявки на заказ вверху страницы в шапке сайте '):
                base_page = BasePage(self.driver)
                base_page.order_button_top_click()
        else:
            with allure.step('Нажимаем на кнопку создания заявки на заказ вверху страницы в шапке сайте '):
                main_page = MainPage(self.driver)
                main_page.scrolling_to_order_button_big_and_click()

        order_page = OrderPage(self.driver)
        with allure.step('Заполнить первую страницу заказа самоката: имя, фамилия, адрес доставки, ближайшую станцию метро и номер телефона'):
            order_page.fill_first_page(order_data)
        with allure.step('Заполнить вторую страницу заказа самоката: Дату доставки, срок аренды, цвет самоката и комментарий курьеру'):
            order_page.fill_second_page(order_data)
        with allure.step('После заполнения формы - открывается модальное окно, в открывшемся окне - нажать кнопку "Да" '):
            order_page.confirm_order()
        with allure.step('При нажатии на кнопку - "Да" появляется сообщение об успешном создании заявки, появляется кнопка "Проверить статус" '):
            assert order_page.check_success_message(), "Сообщение об успешном заказе не появилось"

    @classmethod
    def teardown_class(cls):
        with allure.step('Закрываем созданный экземпляр браузерного клиента'):
            cls.driver.quit()