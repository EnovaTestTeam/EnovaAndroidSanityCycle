from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    EMAIL = (By.ID, "com.harman.enova.beta:id/emailEditText")
    SERVER = (By.ID, "com.harman.enova.beta:id/selectHostButton")
    PROTOCOL = (By.ID, "com.harman.enova.beta:id/selectProtocolButton")
    SEND_BUTTON = (By.ID, "com.harman.enova.beta:id/submitBtn")
    SERVERS_LIST = (By.ID, "com.harman.enova.beta:id/serverName")
    PROTOCOL_LIST = (By.ID, "com.harman.enova.beta:id/protocolName")
    SKIP_SETTINGS_BUTTON = (By.ID, "com.harman.enova.beta:id/continueButton")
    REGISTRATION_TITLE = (By.ID, "com.harman.enova.beta:id/registrationTitle")
    WARNING_INCORRECT_EMAIL = (By.ID, "com.harman.enova.beta:id/errorText")
    CUSTOMERS_LANGUAGE_LIST = (By.ID, "com.harman.enova.beta:id/customerLanguage")
    LANGUAGES = (By.ID, "com.harman.enova.beta:id/languageName")

    def __init__(self, driver):
        super().__init__(driver)

    def is_login_page(self):
        if self.is_element_by_locator(self.REGISTRATION_TITLE) or self.is_element_by_locator(self.SEND_BUTTON):
            return True
        else:
            return False

    def set_email(self, user_name):
        self.send_keys_by_locator(self.EMAIL, user_name)

    def set_server(self, server_name):
        self.click_by_locator(self.SERVER)
        elements = self.find_elements(self.SERVERS_LIST)
        for element in elements:
            if self.get_element_text_by_element(element) == server_name:
                self.click_by_element(element)
                break

    def set_protocol(self, protocol):
        self.click_by_locator(self.PROTOCOL)
        elements = self.find_elements(self.PROTOCOL_LIST)
        for element in elements:
            if self.get_element_text_by_element(element) == protocol:
                self.click_by_element(element)
                break

    def click_send_button(self):
        self.click_by_locator(self.SEND_BUTTON)

    def is_warning_red_text(self):
        if self.is_element_by_locator(self.WARNING_INCORRECT_EMAIL):
            return True
        else:
            return False

    def change_language_skip_settings(self, language):
        continue_button = self.find_element(self.SKIP_SETTINGS_BUTTON)
        self.click_by_element(continue_button)
        self.select_language_after_login(language)
        continue_button = self.find_element(self.SKIP_SETTINGS_BUTTON)
        self.click_by_element(continue_button)

    def select_language_after_login(self, language):
        customers_language_list = self.find_elements(self.CUSTOMERS_LANGUAGE_LIST)
        for i in range(len(customers_language_list)):
            element = self.find_elements(self.CUSTOMERS_LANGUAGE_LIST)[i]
            if self.get_element_text_by_element(element) == language:
                continue
            self.click_by_element(element)
            languages = self.find_elements(self.LANGUAGES)
            for lang in languages:
                if self.get_element_text_by_element(lang) == language:
                    self.click_by_element(lang)
                    break

    def login(self, server_name, user_name, protocol, language):
        self.set_email(user_name)
        self.set_server(server_name)
        self.set_protocol(protocol)
        self.click_send_button()
        self.change_language_skip_settings(language)
