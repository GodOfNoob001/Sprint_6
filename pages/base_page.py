from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import LocatorsBasePage


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def yandex_logo_click(self):
        self.driver.find_element(*LocatorsBasePage.YANDEX_LOGO_BUTTON).click()

    @allure.step('Ждать конкретный URL')
    def wait_for_url(self, url, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.url_to_be(url)
        )

    @allure.step('Ждать URL содержащий текст')
    def wait_for_url_contains(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.url_contains(text)
        )

    @allure.step('Ждать новое окно и переключиться')
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

    @allure.step('Ждать видимости элемента')
    def wait_for_element_visible(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ждать кликабельности элемента')
    def wait_for_element_clickable(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Проверить видимость элемента')
    def is_element_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False


    @allure.step('Найти элемент с ожиданием')
    def find_element(self, locator, timeout=10):
        timeout = timeout or self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located(locator)
        )


    @allure.step('Кликнуть на элемент')
    def click(self, locator, timeout=10):
        element = self.wait_for_element_clickable(locator, timeout)
        element.click()

    @allure.step('Ввести текст в элемент')
    def send_keys_to_element(self, locator, text, timeout=10):
        element = self.wait_for_element_visible(locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step('Получить текст элемента')
    def get_element_text(self, locator, timeout=10):
        element = self.wait_for_element_visible(locator, timeout)
        return element.text

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Выполнить JavaScript')
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    @allure.step('Проскроллиить к элементу')
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element_visible(locator, timeout)
        self.execute_script("arguments[0].scrollIntoView(true);", element)
