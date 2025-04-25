from selenium.webdriver.common.by import By

class UrbanRoutesLocators:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    call_taxi_button = (By.CSS_SELECTOR, ".button.round")
    comfort_fare_option = (By.XPATH, '//*[@id="root"]//div[contains(text(), "Comfort")]')
    phone_number_button = (By.CLASS_NAME, "np-text")
    phone_number_input = (By.ID, "phone")