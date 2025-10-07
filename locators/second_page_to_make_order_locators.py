from selenium.webdriver.common.by import By


class LocatorsSecondPageOrder:
    DATE_OF_DELIVERY_INPUT = [By.XPATH, '//input[@placeholder = "* Когда привезти самокат"]']
    RENTAL_PERIOD_DROPDOWN = [By.CLASS_NAME, 'Dropdown-control']
    RENTAL_PERIOD_DROPDOWN_MENU = [By.CLASS_NAME, 'Dropdown-menu']
    RENTAL_PERIOD_1_DAY = [By.XPATH, '//div[@class="Dropdown-option" and text()="сутки"]']
    RENTAL_PERIOD_7_DAYS = [By.XPATH, '//div[@class="Dropdown-option" and text()="семеро суток"]']
    BLACK_COLOR_CHECKBOX = [By.ID, 'black']
    GREY_COLOR_CHECKBOX = [By.ID, 'grey']
    COMMENT_FOR_DELIVERER = [By.XPATH, '//input[@placeholder = "Комментарий для курьера"]']
    ORDER_BUTTON = [By.XPATH, '//div[contains(@class, "Order_Content")]//button[text()="Заказать"]']
