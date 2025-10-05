from selenium.webdriver.common.by import By

class LocatorsFirstPageOrder:
    NAME_INPUT_LOCATOR = [By.XPATH, "//input[@placeholder ='* Имя']"]
    SECOND_NAME_INPUT_LOCATOR = [By.XPATH, "//input[@placeholder = '* Фамилия']"]
    ADDRESS_INPUT_LOCATOR = [By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']"]
    METRO_INPUT_LOCATOR = [By.XPATH, "//input[@placeholder = '* Станция метро']"]
    PHONE_INPUT_LOCATOR = [By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']"]
    NEXT_PAGE_BUTTON = [By.XPATH, "//button[contains(text(), 'Далее')]"]
