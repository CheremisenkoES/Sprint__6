import pytest
import allure
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from data.order_page_data import OrderData
from pages.order_page import OrderPage
from pages.main_page import MainPage

@allure.feature('Заказ самоката')
class TestScooterOrder:

    @allure.title('Тест заказа доставки самоката')
    @allure.description(
        'Кликнуть на кнопку "Заказать" > заполнить форму валидными данными > появляется окно "Посмотреть статус" '
    )
    @pytest.mark.parametrize(
        'order_button, customer_data, metro_button, rental_data, days_button, colour_button',
        [
            [MainPageLocators.header_order_button, OrderData.user_kit_one, OrderPageLocators.metro_zorge_st,
             OrderData.terms_one, OrderPageLocators.one_day_period, OrderPageLocators.scooter_colour_black],
            [MainPageLocators.center_order_button, OrderData.user_kit_two, OrderPageLocators.metro_lubjanka_st,
             OrderData.terms_two, OrderPageLocators.four_day_period, OrderPageLocators.scooter_colour_gray]
        ]
    )
    def test_scooter_orders(self, driver, order_button, customer_data, metro_button, rental_data,
                            days_button, colour_button):
        main_page = MainPage(driver)
        main_page.click_order_button(order_button)
        order_page = OrderPage(driver)
        order_page.fill_out_customer_form(*customer_data, metro_button)
        order_page.click_next_button()
        order_page.fill_out_rental_form(*rental_data, days_button, colour_button)
        order_page.click_order_button()
        order_page.wait_for_load_order_header()
        order_page.click_yes_button()
        order_page.check_success_window()