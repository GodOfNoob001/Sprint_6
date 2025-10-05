from selenium.webdriver.common.by import By

class LocatorsSuccessOrderScreen:
    SUCCESS_MESSAGE = [By.XPATH, '//div[contains(text(), "Заказ оформлен")]']
    CHECK_ORDER_BUTTON = [By.XPATH, '//div[contains(text(), "Номер заказа")]']