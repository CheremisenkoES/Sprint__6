import pytest
import allure
from locators.main_page_locators import MainPageLocators
from data.main_page_data import FaqAnswersData
from pages.main_page import MainPage

@allure.feature('FAQ на главной странице "Яндекс Самокат"')
class TestFaqHomePage:

    @allure.title('Тест открытия ответов в FAQ')
    @allure.description('Клик по вопросам FAQ по очереди > открываются ответы на вопросы по очереди')
    @pytest.mark.parametrize(
        'button, answer, expected_text',
        [
            [MainPageLocators.coast_question_button, MainPageLocators.coast_answer_text,
             FaqAnswersData.coast_ans],
            [MainPageLocators.share_question_button, MainPageLocators.share_answer_text,
             FaqAnswersData.share_ans],
            [MainPageLocators.time_rent_question_button, MainPageLocators.time_rent_answer_text,
             FaqAnswersData.time_rent_ans],
            [MainPageLocators.today_rent_question_button, MainPageLocators.today_rent_answer_text,
             FaqAnswersData.today_rent_ans],
            [MainPageLocators.extend_return_question_button, MainPageLocators.extend_return_answer_text,
             FaqAnswersData.extend_return_ans],
            [MainPageLocators.charge_question_button, MainPageLocators.charge_answer_text,
             FaqAnswersData.charge_ans],
            [MainPageLocators.cancel_order_question_button, MainPageLocators.cancel_order_answer_text,
             FaqAnswersData.cancel_order_ans],
            [MainPageLocators.mkad_question_button, MainPageLocators.mkad_answer_text,
             FaqAnswersData.mkad_ans]
        ]
    )
    def test_faq_list_click_on_questions_check_answer_(self, driver, button, answer, expected_text):
        main_page = MainPage(driver)
        main_page.click_question_button(button)
        main_page.check_answer_text(answer, expected_text)