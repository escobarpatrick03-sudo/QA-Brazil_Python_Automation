import time

import data
import helpers

from pages import UrbanRoutesPage
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = Chrome()
        cls.driver.implicitly_wait(5)

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução")

    def setup_method(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page = UrbanRoutesPage(self.driver)

    def _start_comfort_flow(self):
        self.page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

    def test_set_route(self):
        self.page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert self.page.get_from_location() == data.ADDRESS_FROM
        assert self.page.get_to_location() == data.ADDRESS_TO

    def test_select_plan(self):
        self.page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.click_taxi_option()
        self.page.click_icon_comfort_selected()

        assert self.page.is_comfort_icon_active()


    def test_fill_phone_number(self):
        self.page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.click_taxi_option()
        self.page.click_number_icon()
        self.page.enter_phone_number(data.PHONE_NUMBER)
        self.page.click_next_button()
        code = helpers.retrieve_phone_code(self.driver)

        assert self.page.enter_phone_number() == data.PHONE_NUMBER

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.click_taxi_option()
        self.page.click_payment_type()
        self.page.click_credit_card_icon()
        self.page.enter_card_number(data.CARD_NUMBER)
        self.page.enter_code_card(data.CARD_CODE)
        self.page.click_add_button()

        assert self.page.get_current_payment_method() == 'Cartão'

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.click_taxi_option()
        self.page.click_icon_comfort_selected()
        self.page.set_message_for_driver(data.MESSAGE_FOR_DRIVER)

        assert self.page.get_message_for_driver() == data.MESSAGE_FOR_DRIVER


    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.click_taxi_option()
        self.page.click_icon_comfort_selected()
        self.page.click_blanket_and_handkerchiefs_option()
        self.page.is_blanket_and_handkerchiefs_option_checked()

        assert self.page.is_blanket_and_handkerchiefs_option_checked()


        print("Função criada para testar pedido de cobertor e lenços")
        pass

    def test_order_2_ice_creams(self):
        self.page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.click_taxi_option()
        self.page.click_icon_comfort_selected()
        self.page.enter_message(data.MESSAGE_FOR_DRIVER)
        self.page.add_icecream(2)
        self.page.get_current_icecream_amount()

        numbers_of_ice_creams = 2
        for count in range(numbers_of_ice_creams):
            print("Função criada para escolher 2 sorvetes")
        pass

        assert self.page.is_get_current()

    def test_car_search_model_appears(self):
        self.page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.click_taxi_option()
        self.page.click_icon_comfort_selected()
        self.page.enter_message(data.MESSAGE_FOR_DRIVER)
        self.page.click_order_taxi()

        assert self.page.is_order_taxi_popup_displayed()

        print("Função criada para testar modelos de carro")
        pass

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
