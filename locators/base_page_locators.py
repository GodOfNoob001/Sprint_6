from selenium.webdriver.common.by import By

class LocatorsBasePage:
    YANDEX_LOGO_BUTTON = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    SCOOTER_LOGO_BUTTON = [By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']"]
    ORDER_BUTTON_TOP = [By.CLASS_NAME, 'Button_Button__ra12g']
    COOKIE_BUTTON = [By.XPATH, "//button[contains(text(), 'да все привыкли')]"]