import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DzenPage(BasePage):
    dzen_logo_in_header = (By.CLASS_NAME, 'desktop-base-header__logo-tA')

    @allure.step('Ожидание загрузки главной страницы "Дзен"')
    def loading_dzen_page(self):
        self.wait_for_visibility_of_element(self.dzen_logo_in_header)

    @allure.step('Проверка открытия страницы "Дзен"')
    def check_go_to_dzen(self):
        current_url = self.get_current_url()
        assert current_url == "https://dzen.ru/?yredirect=true", 'Главная страница "Дзен" не открылась'