import allure
from selenium.webdriver import Keys
from locators.first_page_to_make_order_locators import LocatorsFirstPageOrder
from selenium.webdriver.common.by import By
from locators.second_page_to_make_order_locators import LocatorsSecondPageOrder
from locators.screen_to_confirm_order_locators import LocatorsConfirmationOrderScreen
from locators.screen_success_confirmation_locators import LocatorsSuccessOrderScreen
from pages.base_page import BasePage

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    @allure.step('Заполнить первую страницу заказа')
    def fill_first_page(self, order_data):
        self.send_keys_to_element(LocatorsFirstPageOrder.NAME_INPUT_LOCATOR, order_data["name"])
        self.send_keys_to_element(LocatorsFirstPageOrder.SECOND_NAME_INPUT_LOCATOR, order_data["surname"])
        self.send_keys_to_element(LocatorsFirstPageOrder.ADDRESS_INPUT_LOCATOR, order_data["address"])
        self.select_metro_station(order_data["metro"])
        self.send_keys_to_element(LocatorsFirstPageOrder.PHONE_INPUT_LOCATOR, order_data["phone"])
        self.click(LocatorsFirstPageOrder.NEXT_PAGE_BUTTON)

    @allure.step('Выбрать станцию метро')
    def select_metro_station(self, station_name):
        self.click(LocatorsFirstPageOrder.METRO_INPUT_LOCATOR)
        self.send_keys_to_element(LocatorsFirstPageOrder.METRO_INPUT_LOCATOR, station_name)
        station_locator = (By.XPATH, f"//div[text()='{station_name}']")
        self.click(station_locator)

    @allure.step('Заполнить вторую страницу заказа')
    def fill_second_page(self, order_data):
        date_input = self.find_element(LocatorsSecondPageOrder.DATE_OF_DELIVERY_INPUT)
        date_input.send_keys(order_data["date"])
        date_input.send_keys(Keys.ENTER)
        self.select_rental_period(order_data["rental_period"])
        self.select_scooter_color(order_data["color"])
        self.send_keys_to_element(LocatorsSecondPageOrder.COMMENT_FOR_DELIVERER, order_data["comment"])
        self.click(LocatorsSecondPageOrder.ORDER_BUTTON)

    @allure.step('Выбрать период аренды')
    def select_rental_period(self, period):
        self.click(LocatorsSecondPageOrder.RENTAL_PERIOD_DROPDOWN)
        period_locators = {
            "сутки": LocatorsSecondPageOrder.RENTAL_PERIOD_1_DAY,
            "семеро суток": LocatorsSecondPageOrder.RENTAL_PERIOD_7_DAYS
        }
        self.click(period_locators[period])

    @allure.step('Выбрать цвет самоката')
    def select_scooter_color(self, color):
        color_locators = {
            "black": LocatorsSecondPageOrder.BLACK_COLOR_CHECKBOX,
            "grey": LocatorsSecondPageOrder.GREY_COLOR_CHECKBOX
        }
        self.click(color_locators[color])

    @allure.step('Подтвердить заказ')
    def confirm_order(self):
        self.click(LocatorsConfirmationOrderScreen.YES_BUTTON)

    @allure.step('Проверить отображение сообщения об успехе')
    def check_success_message(self):
        return (self.is_element_visible(LocatorsSuccessOrderScreen.SUCCESS_MESSAGE) and
                self.is_element_visible(LocatorsSuccessOrderScreen.CHECK_ORDER_BUTTON))