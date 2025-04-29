from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import data
import helpers
from UrbanRoutesLocators import UrbanRoutesLocators

class UrbanRoutesPage:

    def __init__(self, driver):
        self.modal_opcional = None
        self.driver = driver
        self.locators = UrbanRoutesLocators

    # Métodos para las direcciones
    def set_from(self, from_address):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.locators.to_field).send_keys(to_address)

    def get_from_value(self):
        return self.driver.find_element(*self.locators.from_field).get_property('value')

    def get_to_value(self):
        return self.driver.find_element(*self.locators.to_field).get_property('value')

    # Pedir un Taxi
    def click_order_taxi_button(self):
        self.driver.find_element(*self.locators.request_taxi_button).click()

    # Tarifa Comfort
    def click_comfort_tariff_button(self):
        comfort_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.tariff_comfort_button)
        )
        comfort_button.click()

    # Teléfono
    def fill_phone_number(self, phone=data.PHONE_NUMBER):
        self.driver.find_element(*self.locators.phone_input).send_keys(phone)

    def click_next_button(self):
        self.driver.find_element(*self.locators.next_button).click()

    def enter_confirmation_code(self):
        code = helpers.retrieve_phone_code(self.driver)
        self.driver.find_element(*self.locators.code_field).send_keys(code)

    def confirm_code(self):
        self.driver.find_element(*self.locators.confirmation_code_button).click()

    def click_phone_method(self):
        self.driver.find_element(*self.locators.phone_method_button).click()

    # Información de pago
    def click_payment_method_field(self):
        self.driver.find_element(*self.locators.phone_method_button).click()

    def click_add_card_button(self):
        self.driver.find_element(*self.locators.add_card_button).click()

    def fill_card_details(self, card_number=data.CARD_NUMBER, card_code=data.CARD_CODE):
        self.driver.find_element(*self.locators.card_number_field).send_keys(card_number)
        card_code_field = self.driver.find_element(*self.locators.card_code_field)
        card_code_field.send_keys(card_code)
        card_code_field.send_keys(Keys.TAB)

    def link_card(self):
        self.driver.find_element(*self.locators.link_card_button).click()

    def close_payment_modal(self):
        self.driver.find_element(*self.locators.close_payment_modal).click()

    # Mensaje al conductor
    def write_new_message(self, message=data.MESSAGE_FOR_DRIVER):
        self.driver.find_element(*self.locators.message_to_driver).send_keys(message)

    # Pedir Manta y pañuelos
    def click_blanket_and_scarves_switch(self):
        self.driver.find_element(*self.locators.blanket_switch).click()

    # Pedir Helados
    def click_add_icecream(self, count=2):
        for _ in range(count):
         self.driver.find_element(*self.locators.add_ice_cream_Button).click()

    # Pedir taxi y esperar modal
    def click_order_a_taxi(self):
        self.driver.find_element(*self.locators.request_taxi_button).click()

    def wait_opcional_modal(self):
        WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.locators.modal_opcional)
        )