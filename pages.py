from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

class UrbanRoutesPage:

    # Seção De e Para
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Fluxo de chamada de táxi
    TAXI_OPTION = (By.XPATH, '//button[contains(text(), "Chamar")]')
    COMFORT_ICON = (By.XPATH, '//img[contains(@src, "kids")]')
    COMFORT_ACTIVE = (By.XPATH, '//*[@class = "tcard active"]')

    # Número de telefone
    PHONE_OPTION = (By.XPATH, '//div[contains(text(), "Número de telefone")]')
    PHONE_INPUT = (By.ID, "phone")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Próximo']")

    # Cartão de crédito
    PAYMENT_METHOD_BUTTON = (By.XPATH, '//div[@class="pp-button filled"]//div[contains(text(), "Método de pagamento")]')
    ADD_CARD_OPTION_BUTTON = (By.XPATH, '//div[contains(text(), "Adicionar cartão")]')
    CARD_NUMBER_INPUT = (By.ID, 'number')
    CARD_CODE_INPUT = (By.XPATH, '//input[@class="card-input" and @id="code"]')
    FINAL_ADD_CARD_BUTTON = (By.XPATH, '//button[contains(text(), "Adicionar")]')
    CURRENT_PAYMENT_METHOD = (By.XPATH, '//div[contains(@class, "pp-value-text")]')

    # Comentário para o motorista
    COMMENT_INPUT = (By.ID, "//*[@id='comment']")


    # Pedir um cobertor e lençois
    BLANKET_AND_HANDKERCHIEFS_OPTION_DIV = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div")
    BLANKET_AND_HANDKERCHIEFS_OPTION_INPUT = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/input")

    # Pedir 2 sorvetes
    ADD_ICECREAM_BUTTON = (By.XPATH, "//div[text()='Sorvete']/following::div[contains(@class, 'counter-plus')][1]")
    CURRENT_ICECREAM_AMOUNT_FIELD = (By.XPATH,"//div[text()='Sorvete']/following::div[contains(@class, 'counter-value')][1]")

    # Pedir táxi opção "Comfort"
    COMFORT_OPTION_BUTTON = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[1]/div[5]")
    ORDER_TAXI_POPUP_FIELD = (By.XPATH, "//*[@id='root']/div/div[3]/div[4]/button ")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Métodos COR POM

    def _find(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def _click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def _type(self, locator, text):
        element = self._find(locator)
        element.clear()
        element.send_keys(text)

    def _press_tab(self):
        self.driver.switch_to.active_element.send_keys(Keys.TAB)


        # Endereço

    def _get_text(self, locator):
        return self._find(locator).text

    def _get_value(self, locator):
        return self._find(locator).get_attribute('value')

    def enter_locations(self, from_text, to_text):
        self._type(self.from_field, from_text)
        self._type(self.to_field, to_text)

    def get_from_location(self):
        return self._get_value(self.from_field)

    def get_to_location(self):
        return self._get_value(self.to_field)

    # Chamar Táxi

    def click_taxi_option(self):
        self._click(self.TAXI_OPTION)

    def click_icon_comfort_selected(self):
        self._click(self.COMFORT_ICON)

    def is_comfort_icon_active(self):
        try:
            active_button = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(self.COMFORT_ACTIVE)
            )
        except:
            return False
        return "active" in active_button.get_attribute("class")

    # Número de telefone

    def click_number_icon(self):
        self._click(self.PHONE_OPTION)

    def enter_phone_number(self, phone_number):
        self._type(self.PHONE_INPUT, phone_number)

    def click_next_button(self):
        self._click(self.NEXT_BUTTON)


    # Cartão de crédito

    def set_card(self, card_number, card_code):

        # Passo 1: Abrir a área de métodos de pagamento.
        self._click(self.PAYMENT_METHOD_BUTTON)

        # Passo 2: Escolher a opção de adicionar cartão.
        self._click(self.ADD_CARD_OPTION_BUTTON)

        # Passo 3: Preencher o número do cartão.
        self._type(self.CARD_NUMBER_INPUT, card_number)

        # Passo 4: Preencher o código de segurança.
        self._type(self.CARD_CODE_INPUT, card_code)

        # Passo 5: Tirar o foco do campo para habilitar o botão de confirmação.
        self._press_tab()

        # Passo 6: Finalizar o cadastro do cartão.
        self._click(self.FINAL_ADD_CARD_BUTTON)

    # Mensagem para motorista

    def set_message_for_driver(self,message):
        self._type(self.MESSAGE_FOR_DRIVER_FIELD, message)

    def get_message_for_driver(self):
        return self._get_value(self.MESSAGE_FOR_DRIVER_FIELD)

    # Pedir cobertor e lençois

    def click_blanket_and_handkerchiefs_option(self):
        # Marca a opção de cobertor e lençóis para a corrida
        self._click(self.BLANKET_AND_HANDKERCHIEFS_OPTION_DIV)

    def is_blanket_and_handkerchiefs_option_checked(self):
        elemento = WebDriverWait(self.driver, timeout=5).until(
            EC.presence_of_element_located(self.BLANKET_AND_HANDKERCHIEFS_OPTION_INPUT)
        )
        return elemento.is_selected()


    # Pedir 2 sorvetes

    def add_icecream(self, amount):
        for _ in range(amount):
            self._click(self.ADD_ICECREAM_BUTTON)

    def get_current_icecream_amount(self):
        return int(self._get_text(self.CURRENT_ICECREAM_AMOUNT_FIELD).strip())

    # Pedir um táxi com a tarifa "Comfort"

    def click_order_taxi(self):
        self._click(self.COMFORT_OPTION_BUTTON)

    def is_order_taxi_popup_displayed(self):
        return self._find(self.ORDER_TAXI_POPUP_FIELD).is_displayed()










