import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from UrbanRoutesMethods import UrbanRoutesPage
import data
import helpers


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls, urban_routes_page=None):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(service=Service(), options=options)
        cls.driver.implicitly_wait(10)
        cls.driver.get(data.URBAN_ROUTES_URL)
        cls.routes_page = urban_routes_page.UrbanRoutesPage(cls.driver)

        # 1. Establecer direcciones de origen y destino.

    def test_set_route(self):
        self.routes_page.set_from(data.ADDRESS_FROM)
        self.routes_page.set_to(data.ADDRESS_TO)
        assert self.routes_page.get_from() == data.ADDRESS_FROM
        assert self.routes_page.get_to() == data.ADDRESS_TO

        # 2. Seleccionar la tarifa "Comfort".

    def test_select_comfort_tariff(self, urban_routes_page=None):
        self.routes_page.set_from(data.ADDRESS_FROM)
        self.routes_page.set_to(data.ADDRESS_TO)
        self.routes_page.click_order_taxi_button()
        self.routes_page.click_comfort_tariff_button()
        comfort_tariff = self.driver.find_elements(*self.routes_page.comfort_tariff_button)
        assert "tcard" in self.driver.find_element(*urban_routes_page.UrbanRoutesPage.
                                                   comfort_tariff_button).get_attribute("class")
        assert comfort_tariff[4].is_enabled()

        # 3. Rellenar el número de teléfono.

    def test_fill_phone_number(self):
        self.routes_page.set_from(data.ADDRESS_FROM)
        self.routes_page.set_to(data.ADDRESS_TO)
        self.routes_page.click_order_taxi_button()
        self.routes_page.click_phone_number_field()
        self.routes_page.fill_in_phone_number()
        self.routes_page.click_next_button()
        code = helpers.retrieve_phone_code(self.driver)
        self.routes_page.set_confirmation_code(code)
        self.routes_page.click_code_confirmation_button()
        phone_input_value = self.driver.find_element(*self.routes_page.phone_input).get_attribute("value")
        assert phone_input_value == data.PHONE_NUMBER

        # 4. Agregar tarjeta de crédito.

    def test_add_credit_card(self):
        self.routes_page.set_from(data.ADDRESS_FROM)
        self.routes_page.set_to(data.ADDRESS_TO)
        self.routes_page.click_order_taxi_button()
        self.routes_page.click_payment_method_field()
        self.routes_page.click_add_card_button()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.routes_page.card_number_field)
        ).send_keys(data.CARD_NUMBER)
        self.routes_page.enter_card_number()
        self.routes_page.enter_card_code()
        self.routes_page.press_tab_key()
        self.routes_page.click_add_button()
        card_input = self.driver.find_elements(*self.routes_page.card_added)[1]
        assert card_input.is_enabled()
        self.routes_page.click_card_close_button()

        # 5. Escribir un mensaje para el controlador.

    def test_write_message(self):
        self.routes_page.set_from(data.ADDRESS_FROM)
        self.routes_page.set_to(data.ADDRESS_TO)
        self.routes_page.click_order_taxi_button()
        self.routes_page.enter_new_message()
        assert self.driver.find_element(*self.routes_page.message).get_property('value') == data.MESSAGE_FOR_DRIVER

        # 6. Pedir manta y pañuelos.

    def test_request_blanket_and_scarves(self, urban_routes_page=None):
        self.routes_page.set_from(data.ADDRESS_FROM)
        self.routes_page.set_to(data.ADDRESS_TO)
        self.routes_page.click_order_taxi_button()
        self.routes_page.click_comfort_tariff_button()
        self.routes_page.click_blanket_and_scarves_switch()
        checkbox = self.driver.find_element(*urban_routes_page.UrbanRoutesPage.switch_checkbox)
        assert checkbox.is_selected() == True

        # 7. Pedir 2 helados.

    def test_request_icecream(self, urban_routes_page=None):
        self.routes_page.set_from(data.ADDRESS_FROM)
        self.routes_page.set_to(data.ADDRESS_TO)
        self.routes_page.click_order_taxi_button()
        self.routes_page.click_comfort_tariff_button()
        self.routes_page.click_add_icecream()
        self.routes_page.click_add_icecream()
        icecream_counter = self.driver.find_element(*urban_routes_page.UrbanRoutesPage.icecream_counter)
        icecream_count = int(icecream_counter.text)
        assert icecream_count == 2

        # 8. Buscar un taxi.

    def test_search_taxi(self):
        self.routes_page.set_from(data.ADDRESS_FROM)
        self.routes_page.set_to(data.ADDRESS_TO)
        self.routes_page.click_order_taxi_button()
        self.routes_page.click_comfort_tariff_button()
        self.routes_page.click_phone_number_field()
        self.routes_page.fill_in_phone_number()
        self.routes_page.click_next_button()
        code = helpers.retrieve_phone_code(self.driver)
        self.routes_page.set_confirmation_code(code)
        self.routes_page.click_code_confirmation_button()
        self.routes_page.click_payment_method_field()
        self.routes_page.click_add_card_button()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.routes_page.card_number_field)
        ).send_keys(data.CARD_NUMBER)
        self.routes_page.enter_card_number()
        self.routes_page.enter_card_code()
        self.routes_page.press_tab_key()
        self.routes_page.click_add_button()
        self.routes_page.click_card_close_button()
        self.routes_page.enter_new_message()
        self.routes_page.click_blanket_and_scarves_switch()
        self.routes_page.click_add_icecream()
        self.routes_page.click_add_icecream()
        self.routes_page.click_order_a_taxi()
        WebDriverWait(self.driver, 40).until(
            expected_conditions.visibility_of_element_located(self.routes_page.modal_opcional)
        )
        assert self.driver.find_element(*self.routes_page.modal_opcional).is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()