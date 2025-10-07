import allure
import pytest
from selenium import webdriver
from data import Data
from conftest import main_page, driver

class TestMainPage:
    @pytest.mark.parametrize("faq_number, expected_question", [
        (1, Data.first_faq_question),
        (2, Data.second_faq_question),
        (3, Data.third_faq_question),
        (4, Data.fourth_faq_question),
        (5, Data.fifth_faq_question),
        (6, Data.sixth_faq_question),
        (7, Data.seventh_faq_question),
        (8, Data.eighth_faq_question)
    ])
    @allure.title('При скролле до FAQ-блока на главной странице - отображаются валидные вопросы')
    @allure.description('В рамках данного тестового прогона проверяется, что при переходе к FAQ-блоку - вопросы отображаются, значения вопросов валидны')
    def test_faq_on_main_page_successfully_got_right_question_text(self, main_page, faq_number, expected_question):
        with allure.step(f'Получаем текст вопроса, отображаемого на странице: {expected_question}'):
            actual_question = main_page.get_faq_question_by_number(faq_number)
        with allure.step(f'Текст вопроса соответсвует ожидаемому: {actual_question}'):
            assert actual_question == expected_question, f"Ожидался текст {expected_question}, а получен {actual_question}"

    @pytest.mark.parametrize("faq_number, expected_question, expected_answer", [
        (1, Data.first_faq_question, Data.first_faq_answer),
        (2, Data.second_faq_question, Data.second_faq_answer),
        (3, Data.third_faq_question, Data.third_faq_answer),
        (4, Data.fourth_faq_question, Data.fourth_faq_answer),
        (5, Data.fifth_faq_question, Data.fifth_faq_answer),
        (6, Data.sixth_faq_question, Data.sixth_faq_answer),
        (7, Data.seventh_faq_question, Data.seventh_faq_answer),
        (8, Data.eighth_faq_question, Data.eighth_faq_answer)
    ])
    @allure.title('При открытии вопросов FAQ - ответы соответствуют теме вопроса')
    @allure.description('В рамках данного тестового прогона проверяется, что при открытии FAQ-вопроса - ответ внутри раскрывшейся панели соответствует тематике вопроса и валиден')
    def test_faq_on_main_page_successfully_got_right_answer_to_right_question(self, main_page, faq_number, expected_question, expected_answer):
        with allure.step(f'Получаем текст ответа к каждому вопросу, отображаемого на странице: {expected_answer}'):
            actual_answer = main_page.get_faq_text_by_number(faq_number)
        with allure.step(f'Текст вопроса соответсвует ожидаемому: {actual_answer}'):
            assert actual_answer == expected_answer, f"Ожидался текст {expected_answer}, а получен {actual_answer}"