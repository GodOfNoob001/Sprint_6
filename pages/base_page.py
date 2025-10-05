from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import LocatorsBasePage


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def yandex_logo_click(self):
        self.driver.find_element(*LocatorsBasePage.YANDEX_LOGO_BUTTON).click()

    def scooter_logo_click(self):
        self.driver.find_element(*LocatorsBasePage.SCOOTER_LOGO_BUTTON).click()

    def order_button_top_click(self):
        self.driver.find_element(*LocatorsBasePage.ORDER_BUTTON_TOP).click()

    def wait_for_url(self, url, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.url_to_be(url)
        )

    def wait_for_url_contains(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.url_contains(text)
        )

    def wait_for_new_window_and_switch(self, timeout=10):
        original_window = self.driver.current_window_handle
        WebDriverWait(self.driver, timeout).until(expected_conditions.number_of_windows_to_be(2))
        for window in self.driver.window_handles:
            if window != original_window:
                self.driver.switch_to.window(window)
                return

    @property
    def current_url(self):
        return self.driver.current_url