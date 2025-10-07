import allure
from locators.base_page_locators import LocatorsBasePage
from locators.main_page_locators import LocatorsMainPage
from pages.base_page import BasePage

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def close_cookie_banner(self):
        cookie_button = WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(LocatorsBasePage.COOKIE_BUTTON))
        cookie_button.click()

    def scrolling_to_order_button_big_and_click(self):
        element = self.driver.find_element(*LocatorsMainPage.ORDER_BUTTON_BIG)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

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
        question_element = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(faq_data["question"]))
        return question_element.text

    def get_faq_text_by_number(self, faq_number):
        faq_data = self.FAQ_MAPPING[faq_number]
        question_element = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(faq_data["question"]))
        question_element.click()
        panel_element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(faq_data["panel"])
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", panel_element)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of(panel_element)
        )
        return panel_element.text



