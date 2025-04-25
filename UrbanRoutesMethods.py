from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from UrbanRoutesLocators import UrbanRoutesLocators

# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.Locators = UrbanRoutesLocators

def set_from(self, from_address):
    #self.driver.find_element(*self.from_field).send_keys(from_address)
    WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.from_field)
        ).send_keys(from_address)

def set_to(self, to_address):
#self.driver.find_element(*self.to_field).send_keys(to_address)
    WebDriverWait(self.driver, 5).until(
           EC.presence_of_element_located(self.to_field)
        ).send_keys(to_address)

def get_from(self):
    return self.driver.find_element(*self.from_field).get_property('value')

def get_to(self):
    return self.driver.find_element(*self.to_field).get_property('value')

def set_route(self, from_address, to_address):
    self.set_from(from_address)
    self.set_to(to_address)

def click_call_taxi_button(self):
    WebDriverWait(self.driver, 5).until(
        EC.element_to_be_clickable(self.locators.call_taxi_button)
    ).click()

def click_on_comfort_fare_option(self):
    WebDriverWait(self.driver, 5).until(
        EC.element_to_be_clickable(self.locators.comfort_fare_option)
    ).click()

def get_comfort_fare_option(self):
    return WebDriverWait(self.driver, 5).until(
        EC.visibility_of_element_located(self.locators.comfort_fare_option)
    )