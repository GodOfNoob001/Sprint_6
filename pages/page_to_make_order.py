from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.first_page_to_make_order_locators import LocatorsFirstPageOrder
from selenium.webdriver.common.by import By
from locators.second_page_to_make_order_locators import LocatorsSecondPageOrder
from locators.screen_to_confirm_order_locators import LocatorsConfirmationOrderScreen
from locators.screen_success_confirmation_locators import LocatorsSuccessOrderScreen


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_first_page(self, order_data):
        self.driver.find_element(*LocatorsFirstPageOrder.NAME_INPUT_LOCATOR).send_keys(order_data["name"])
        self.driver.find_element(*LocatorsFirstPageOrder.SECOND_NAME_INPUT_LOCATOR).send_keys(order_data["surname"])
        self.driver.find_element(*LocatorsFirstPageOrder.ADDRESS_INPUT_LOCATOR).send_keys(order_data["address"])
        self.select_metro_station(order_data["metro"])
        self.driver.find_element(*LocatorsFirstPageOrder.PHONE_INPUT_LOCATOR).send_keys(order_data["phone"])
        self.driver.find_element(*LocatorsFirstPageOrder.NEXT_PAGE_BUTTON).click()

    def select_metro_station(self, station_name):
        metro_input = self.driver.find_element(*LocatorsFirstPageOrder.METRO_INPUT_LOCATOR)
        metro_input.click()
        metro_input.send_keys(station_name)
        station_option = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, f"//div[text()='{station_name}']"))
        )
        station_option.click()

    def fill_second_page(self, order_data):
        date_input = self.driver.find_element(*LocatorsSecondPageOrder.DATE_OF_DELIVERY_INPUT)
        date_input.send_keys(order_data["date"])
        date_input.send_keys(Keys.ENTER)
        self.select_rental_period(order_data["rental_period"])
        self.select_scooter_color(order_data["color"])
        comment_input = self.driver.find_element(*LocatorsSecondPageOrder.COMMENT_FOR_DELIVERER)
        comment_input.send_keys(order_data["comment"])
        self.driver.find_element(*LocatorsSecondPageOrder.ORDER_BUTTON).click()


    def select_rental_period(self, period):
        dropdown = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(LocatorsSecondPageOrder.RENTAL_PERIOD_DROPDOWN)
        )
        dropdown.click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(LocatorsSecondPageOrder.RENTAL_PERIOD_DROPDOWN_MENU)
        )
        period_locators = {
            "сутки": LocatorsSecondPageOrder.RENTAL_PERIOD_1_DAY,
            "семеро суток": LocatorsSecondPageOrder.RENTAL_PERIOD_7_DAYS
        }

        period_element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(period_locators[period])
        )
        period_element.click()

    def select_scooter_color(self, color):
        color_locators = {
            "black": LocatorsSecondPageOrder.BLACK_COLOR_CHECKBOX,
            "grey": LocatorsSecondPageOrder.GREY_COLOR_CHECKBOX
        }

        color_checkbox = self.driver.find_element(*color_locators[color])
        color_checkbox.click()

    def confirm_order(self):
        confirm_button = self.driver.find_element(*LocatorsConfirmationOrderScreen.YES_BUTTON)
        confirm_button.click()

    def check_success_message(self):
        success_message = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(LocatorsSuccessOrderScreen.SUCCESS_MESSAGE)
        )
        success_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(LocatorsSuccessOrderScreen.CHECK_ORDER_BUTTON)
        )
        if success_message.is_displayed() and success_button.is_displayed():
            return True
        else:
            return False
