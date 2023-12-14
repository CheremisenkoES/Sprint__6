from selenium.webdriver.common.by import By


class OrderPageLocators:
    # имя формы заказа "Для кого самокат"
    order_header = (By.CLASS_NAME, 'Order_Header__BZXOb')
    # Поле "Имя"
    firs_name_field = (By.CSS_SELECTOR, '[placeholder="* Имя"]')
    # Поле "Фамилия"
    second_name_field = (By.CSS_SELECTOR, '[placeholder="* Фамилия"]')
    # Поле "Адрес: Куда привезти заказ"
    address_field = (By.CSS_SELECTOR, '[placeholder="* Адрес: куда привезти заказ"]')
    # Поле "Станция метро"
    metro_station = (By.CSS_SELECTOR, '[placeholder="* Станция метро"]')
    # Поле "Телефон: на него позвонит курьер"
    phone_field = (By.CSS_SELECTOR, '[placeholder="* Телефон: на него позвонит курьер"]')
    # Кнопка "Далее"
    next_button = (By.XPATH, '//button[text()="Далее"]')
    # Станция метро "Черкизовская"
    metro_zorge_st = (By.XPATH, '//div[text()="Зорге"]')
    # Станция метро "Курская"
    metro_lubjanka_st = (By.XPATH, '//div[text()="Лубянка"]')
    # имя формы заказа "Про аренду"
    rent_form_header = (By.CLASS_NAME, 'Order_Header__BZXOb')
    # Поле "Когда привезти самокат"
    rent_date_field = (By.CSS_SELECTOR, '[placeholder="* Когда привезти самокат"]')
    # Поле "Срок аренды"
    rent_period_field = (By.CLASS_NAME, 'Dropdown-placeholder')
    # выпадающий список срока аренды "сутки"
    one_day_period = (By.XPATH, '//div[text() = "сутки"]')
    # выпадающий список срока аренды "четверо суток"
    four_day_period = (By.XPATH, '//div[text() = "четверо суток"]')
    # чек-бокс цвета самоката "чёрный"
    scooter_colour_black = (By.ID, 'black')
    # чек-бокс цвета самоката "серый"
    scooter_colour_gray = (By.ID, 'grey')
    # Поле "Комментарий для курьера"
    comment_field = (By.CSS_SELECTOR, '[placeholder="Комментарий для курьера"]')
    # Кнопка "заказать"
    order_button = (By.XPATH, '//div[@class = "Order_Buttons__1xGrp"]/button[text()="Заказать"]')
    # поп-ап "Хотите оформить заказ?"
    popup_order_header = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
    # Кнопка "Да" в поп-апе "Хотите оформить заказ?"
    popup_yes_button = (By.XPATH, '//button[text()="Да"]')
    # Кнопка "Посмотреть статус" в форме "Заказ оформлен"
    popup_status_button = (By.XPATH, '//button[text()="Посмотреть статус"]')
    # Логотип "Самокат"
    logo_scooter = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')