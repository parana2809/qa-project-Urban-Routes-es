from selenium.webdriver.common.by import By

class UrbanRoutesLocators:

    # Direcciones
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Botones Principales
    request_taxi_button = (By.XPATH, '//*[contains(text(), "Pedir un taxi")]')
    tariff_comfort_button = (By.CLASS_NAME, 'tcard')

    # Teléfono
    phone_method_button = (By.CLASS_NAME, "np-button")
    phone_input = (By.ID, 'phone')
    next_button = (By.XPATH, '//*[contains(text(), "Siguiente")]')

    # Confirmación del teléfono
    code_field = (By.ID, 'code')
    confirmation_code_button = (By.XPATH, '//*[contains(text(), "Confirmar")]')

    # Información de pago
    payment_method_button = (By.CLASS_NAME, "pp-button")
    add_card_button = (By.XPATH, '//*[contains(text(), "Agregar tarjeta")]')
    card_number_field = (By.NAME, 'number')
    card_code_field = (By.NAME, 'code')
    link_card_button = (By.XPATH, '//button[text()="Agregar"]')
    close_payment_modal = (By.CSS_SELECTOR, '.payment-picker.open .modal .section.active .close-button')

    # Mensaje al conductor
    message_to_driver = (By.ID, 'comment')

    # Pedir Manta y Pañuelos
    blanket_switch = (By.CLASS_NAME, "switch")

    # Pedir Helado
    add_ice_cream_Button = (By.CLASS_NAME, "counter-plus")
    ice_cream_counter = (By.CLASS_NAME, "counter-value")

    # Modal opcional
    modal_opcional = (By.XPATH, '//*[contains(text(), "El conductor llegará en")]')
    switch_checkbox = (By.CLASS_NAME, "switch-input")
    icecream_counter = (By.CLASS_NAME, "counter-value")




    card_added = (By.CLASS_NAME, 'pp-row')
    ice_cream_counter = (By.CLASS_NAME, "smart-button-wrapper")