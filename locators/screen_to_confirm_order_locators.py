from selenium.webdriver.common.by import By


class LocatorsConfirmationOrderScreen:
    YES_BUTTON = [By.XPATH, '//button[text()="Да"]']
    NO_BUTTON = [By.XPATH, '//button[text()="Нет"]']
