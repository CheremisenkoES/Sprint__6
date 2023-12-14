import allure
from selenium.webdriver import Keys
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Ожидание загрузки окна "Для кого самокат"')
    def wait_for_load_customer_window(self):
        self.wait_for_visibility_of_element(OrderPageLocators.order_header)

    @allure.step('Заполнение поля "Имя"')
    def set_name(self, name):
        self.send_keys(OrderPageLocators.firs_name_field, name)

    @allure.step('Заполнение поля "Фамилия"')
    def set_surname(self, surname):
        self.send_keys(OrderPageLocators.second_name_field, surname)

    @allure.step('Заполнение поля "Адрес"')
    def set_address(self, address):
        self.send_keys(OrderPageLocators.address_field, address)

    @allure.step('Клик на список "Станция метро"')
    def click_metro_field(self):
        self.click_on_element(OrderPageLocators.metro_station)

    @allure.step('Выбор станции метро в списке')
    def choose_metro(self, metro):
        self.scroll(metro)
        self.wait_for_element_to_be_clickable(metro)
        self.click_on_element(metro)

    @allure.step('Заполнение поля "Телефон"')
    def set_phone(self, phone):
        self.send_keys(OrderPageLocators.phone_field, phone)

    @allure.step('Заполнение формы "Для кого самокат"')
    def fill_out_customer_form(self, name, surname, address, phone, metro):
        self.wait_for_load_customer_window()
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.click_metro_field()
        self.choose_metro(metro)
        self.set_phone(phone)

    @allure.step('Клик на кнопку "Далее" формы "Для кого самокат"')
    def click_next_button(self):
        self.click_on_element(OrderPageLocators.next_button)

    @allure.step('Ожидание загрузки окна "Про аренду"')
    def wait_for_load_rental_window(self):
        self.wait_for_visibility_of_element(OrderPageLocators.rent_form_header)

    @allure.step('Заполнение поля "Дата аренды"')
    def set_date(self, date):
        self.send_keys(OrderPageLocators.rent_date_field, date)
        self.send_keys(OrderPageLocators.rent_date_field, Keys.ENTER)

    @allure.step('Клик на поле"Срок аренды"')
    def click_period_field(self):
        self.click_on_element(OrderPageLocators.rent_period_field)

    @allure.step('Выбор срока аренды')
    def click_days_button(self, days_button):
        self.click_on_element(days_button)

    @allure.step('Выбор цвета самоката')
    def click_colour_button(self, colour_button):
        self.click_on_element(colour_button)

    @allure.step('Заполнение поля "Комментарий для курьера"')
    def set_comment(self, comment):
        self.send_keys(OrderPageLocators.comment_field, comment)

    @allure.step('Заполнение формы "Про аренду"')
    def fill_out_rental_form(self, date, comment, days_button, colour_button):
        self.wait_for_load_rental_window()
        self.set_date(date)
        self.click_period_field()
        self.click_days_button(days_button)
        self.click_colour_button(colour_button)
        self.set_comment(comment)

    @allure.step('Клик на кнопку "Заказать"')
    def click_order_button(self):
        self.click_on_element(OrderPageLocators.order_button)

    @allure.step('Ожидание загрузки окна "Хотите оформить заказ?"')
    def wait_for_load_order_header(self):
        self.wait_for_visibility_of_element(OrderPageLocators.popup_order_header)

    @allure.step('Клик на кнопку "Да" в форме "Хотите оформить заказ?"')
    def click_yes_button(self):
        self.click_on_element(OrderPageLocators.popup_yes_button)

    @allure.step('Проверка появления окна создания заказа с кнопкой "Посмотреть статус"')
    def check_success_window(self):
        self.wait_for_visibility_of_element(OrderPageLocators.popup_status_button)
        actually_text = self.get_actually_text(OrderPageLocators.popup_status_button)
        assert actually_text == 'Посмотреть статус', 'Окно создания заказа с кнопкой "Посмотреть статус" не появилось'

    @allure.step('Клик на логотип "Самокат"')
    def click_scooter_logo(self):
        self.wait_for_element_to_be_clickable(OrderPageLocators.logo_scooter)
        self.click_on_element(OrderPageLocators.logo_scooter)