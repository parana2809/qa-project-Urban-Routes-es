import data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from UrbanRoutesMethods import UrbanRoutesPage

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(service=Service(), options=options)

    # 1. Configurar la dirección o ruta (Desde-Hasta)
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    # 2. Seleccionar la tarifa Comfort
    def test_select_comfort_rate(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_call_taxi_button()
        routes_page.click_on_comfort_fare_option()

        comfort_fare = routes_page.get_comfort_fare_option().text
        comfort_text = "Comfort"
        assert comfort_fare in comfort_text

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
