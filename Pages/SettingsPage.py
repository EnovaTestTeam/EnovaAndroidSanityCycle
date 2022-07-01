from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class SettingsInApp(BasePage):
    SETTINGS_BUTTON = (By.ID, "com.harman.enova.beta:id/settingsBtn")
    SETTINGS_DEVICE = (By.ID, "com.harman.enova.beta:id/settings_device")
    CURRENT_SERVER = (By.ID, "com.harman.enova.beta:id/serverName")
    SETTINGS_BACK_BUTTON = (By.ID, "com.harman.enova.beta:id/backButton")
    SETTINGS_COMMON = (By.ID, "com.harman.enova.beta:id/settings_common")
    PAUSE_DETECTION_TIMEOUT = (By.ID, "com.harman.enova.beta:id/pauseDetectionTimeoutLayout")
    TIMEOUT_FIELD = (By.ID, "com.harman.enova.beta:id/inputField")
    TIMEOUT_SAVE_BUTTON = (By.ID, "android:id/button1")
    AUDIOSTREAMING_SWITCH = (By.ID, "com.harman.enova.beta:id/audioStreamingSwitch")
    TRANSCRIBE_MODE_SWITCH = (By.ID, "com.harman.enova.beta:id/transcribeModeSwitch")
    SETTINGS_LANGUAGE = (By.ID, "com.harman.enova.beta:id/settings_language")
    SWITCH_DEFAULT_LANGUAGE = (By.ID, "com.harman.enova.beta:id/switchDefaultLanguage")
    CUSTOMERS_LIST = (By.ID, "com.harman.enova.beta:id/customerName")
    LANGUAGES_LIST = (By.ID, "com.harman.enova.beta:id/languageName")
    UNREGISTER_DEVICE_BUTTON = (By.ID, "com.harman.enova.beta:id/unregisterDevice")
    PRIVACY_POLICY_BUTTON = (By.ID, "com.harman.enova.beta:id/settings_privacy_policy")
    PRIVACY_POLICY_CONTENT = (By.ID, "android:id/content")
    SETTINGS_MAIN_HEADER = (By.ID, "com.harman.enova.beta:id/settings_main_header")
    SHOW_METRICS_SWITCH = (By.ID, "com.harman.enova.beta:id/showMetricsSwitch")
    SHOW_VERSIONS_SWITCH = (By.ID, "com.harman.enova.beta:id/showComponentVersionsSwitch")
    MAX_AUDIO_LENGTH = (By.ID, "com.harman.enova.beta:id/maxAudioLengthTitle")
    EXPORT_METRICS = (By.ID, "com.harman.enova.beta:id/exportMetrics")

    def __init__(self, driver):
        super().__init__(driver)

    def open_settings(self):
        self.click_by_locator(self.SETTINGS_BUTTON)

    def open_device_settings(self):
        self.click_by_locator(self.SETTINGS_BUTTON)
        self.click_by_locator(self.SETTINGS_DEVICE)

    def open_common_settings(self):
        self.click_by_locator(self.SETTINGS_BUTTON)
        self.click_by_locator(self.SETTINGS_COMMON)

    def scroll_common_settings(self):
        self.swipe_top()

    def open_language_settings(self):
        self.click_by_locator(self.SETTINGS_BUTTON)
        self.click_by_locator(self.SETTINGS_LANGUAGE)

    def return_to_customer_screen(self):
        self.click_by_locator(self.SETTINGS_BACK_BUTTON)
        self.click_by_locator(self.SETTINGS_BACK_BUTTON)

    def unregister_device(self):
        self.open_device_settings()
        self.click_by_locator(self.UNREGISTER_DEVICE_BUTTON)

    def get_server(self):
        self.open_device_settings()
        server = self.find_element(self.CURRENT_SERVER)
        server_name = self.get_element_text_by_element(server).split(":")
        print(server_name)
        self.return_to_customer_screen()
        return server_name[0]

    def set_common_pause_timeout(self, pauseDetectionTimeoutLayout):
        self.open_common_settings()
        self.click_by_locator(self.PAUSE_DETECTION_TIMEOUT)
        timeout_field = self.find_element(self.TIMEOUT_FIELD)
        self.clear_element_by_element(timeout_field)
        self.send_keys_by_element(timeout_field, pauseDetectionTimeoutLayout)
        self.click_by_locator(self.TIMEOUT_SAVE_BUTTON)
        self.return_to_customer_screen()

    def set_common_audiostreaming_turn_on(self):
        self.open_common_settings()
        self.click_by_locator(self.AUDIOSTREAMING_SWITCH)
        self.return_to_customer_screen()

    def set_common_transcribe_turn_on(self):
        self.open_common_settings()
        self.click_by_locator(self.TRANSCRIBE_MODE_SWITCH)
        self.return_to_customer_screen()

    def change_language(self, customer, language):
        self.open_language_settings()
        switch_default_language = self.find_element(self.SWITCH_DEFAULT_LANGUAGE)
        if self.is_element_checked_by_element(switch_default_language):
            self.click_by_element(switch_default_language)
        customers = self.find_elements(self.CUSTOMERS_LIST)
        for element in customers:
            if self.get_element_text_by_element(element) == customer:
                self.click_by_element(element)
                break
        languages = self.find_elements(self.LANGUAGES_LIST)
        for element in languages:
            if self.get_element_text_by_element(element) == language:
                self.click_by_element(element)
                break
        self.return_to_customer_screen()

    def open_privacy_policy(self):
        self.open_settings()
        self.click_by_locator(self.PRIVACY_POLICY_BUTTON)

    def is_privacy_policy(self):
        if self.is_element_by_locator(self.PRIVACY_POLICY_CONTENT):
            return True
        else:
            return False

    def close_privacy_policy(self):
        self.click_back_android()

    def show_metrix_switch_on(self):
        self.open_common_settings()
        self.scroll_common_settings()
        if not self.is_element_checked_by_locator(self.SHOW_METRICS_SWITCH):
            self.click_by_locator(self.SHOW_METRICS_SWITCH)
        self.return_to_customer_screen()

    def show_metrix_switch_off(self):
        self.open_common_settings()
        self.scroll_common_settings()
        if self.is_element_checked_by_locator(self.SHOW_METRICS_SWITCH):
            self.click_by_locator(self.SHOW_METRICS_SWITCH)
        self.return_to_customer_screen()

    def show_versions_switch_on(self):
        self.open_common_settings()
        self.scroll_common_settings()
        if not self.is_element_checked_by_locator(self.SHOW_VERSIONS_SWITCH):
            self.click_by_locator(self.SHOW_VERSIONS_SWITCH)
        self.return_to_customer_screen()

    def show_versions_switch_off(self):
        self.open_common_settings()
        self.scroll_common_settings()
        if self.is_element_checked_by_locator(self.SHOW_VERSIONS_SWITCH):
            self.click_by_locator(self.SHOW_VERSIONS_SWITCH)
        self.return_to_customer_screen()
