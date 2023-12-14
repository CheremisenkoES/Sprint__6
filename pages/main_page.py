import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик на кнопку «Заказать»')
    def click_order_button(self, button):
        self.scroll(button)
        self.wait_for_element_to_be_clickable(button)
        self.click_on_element(button)

    @allure.step('Проверка открытия страницы "Яндекс Самокат"')
    def check_go_to_home_page(self):
        current_url = self.get_current_url()
        assert current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.step('Клик на логотип "Яндекс"')
    def click_yandex_logo(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.yandex_logo)
        self.click_on_element(MainPageLocators.yandex_logo)

    @allure.step('Переход на страницу "Дзен"')
    def go_to_dzen(self):
        self.switch_to_window()

    @allure.step('Клик на вопрос')
    def click_question_button(self, button):
        self.scroll(button)
        self.wait_for_element_to_be_clickable(button)
        self.click_on_element(button)

    @allure.step('Проверка открытия текста ответа на выбранный вопрос')
    def check_answer_text(self, answer, expected_text):
        self.wait_for_visibility_of_element(answer)
        actually_text = self.get_actually_text(answer)
        assert actually_text == expected_text