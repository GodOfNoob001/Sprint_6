import allure
from locators.base_page_locators import LocatorsBasePage
from locators.main_page_locators import LocatorsMainPage
from pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Закрыть баннер куки для доступа ко всем элементам страницы')
    def close_cookie_banner(self):
        self.click(LocatorsBasePage.COOKIE_BUTTON, timeout= 5)

    def scrolling_to_order_button_big_and_click(self):
        self.scroll_to_element(LocatorsMainPage.ORDER_BUTTON_BIG)
        self.click(LocatorsMainPage.ORDER_BUTTON_BIG)

    FAQ_MAPPING = {
        1: {"question": LocatorsMainPage.FIRST_FAQ, "panel": LocatorsMainPage.FIRST_FAQ_PANEL},
        2: {"question": LocatorsMainPage.SECOND_FAQ, "panel": LocatorsMainPage.SECOND_FAQ_PANEL},
        3: {"question": LocatorsMainPage.THIRD_FAQ, "panel": LocatorsMainPage.THIRD_FAQ_PANEL},
        4: {"question": LocatorsMainPage.FOURTH_FAQ, "panel": LocatorsMainPage.FOURTH_FAQ_PANEL},
        5: {"question": LocatorsMainPage.FIFTH_FAQ, "panel": LocatorsMainPage.FIFTH_FAQ_PANEL},
        6: {"question": LocatorsMainPage.SIXTH_FAQ, "panel": LocatorsMainPage.SIXTH_FAQ_PANEL},
        7: {"question": LocatorsMainPage.SEVENTH_FAQ, "panel": LocatorsMainPage.SEVENTH_FAQ_PANEL},
        8: {"question": LocatorsMainPage.EIGHTH_FAQ, "panel": LocatorsMainPage.EIGHTH_FAQ_PANEL},
    }
    def get_faq_question_by_number(self, faq_number):
        faq_data = self.FAQ_MAPPING[faq_number]
        return self.get_element_text(faq_data["question"])

    def get_faq_text_by_number(self, faq_number):
        faq_data = self.FAQ_MAPPING[faq_number]
        self.click(faq_data["question"])
        panel_element = self.get_element_text(faq_data["panel"])
        self.scroll_to_element(faq_data["panel"])
        return panel_element

    @allure.step('Нажать на логотип "Яндекс"')
    def yandex_logo_click(self):
        self.click(LocatorsBasePage.YANDEX_LOGO_BUTTON)
    @allure.step('Нажать на логотип "Самокат"')
    def scooter_logo_click(self):
        self.click(LocatorsBasePage.SCOOTER_LOGO_BUTTON)
    @allure.step('Нажать кнопку "Заказать" в шапке веб-сервиса')
    def order_button_top_click(self):
        self.click(LocatorsBasePage.ORDER_BUTTON_TOP)

