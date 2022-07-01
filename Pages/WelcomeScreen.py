from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
import re

class WelcomeScreen(BasePage):

    SETTINGS_ICON = (By.ID, 'settingsBtn')
    BUILD_NUMBER = (By.ID, 'versionName')
    MAIN_TITLE = (By.ID, 'titleTextView')
    CUSTOMER_NAME = (By.ID, 'titleTextView')
    CUSTOMER_DESCRIPTION = (By.ID, 'descriptionTextView')
    SETTINGS_TITLE = (By.ID, 'titleText')
    CUSTOMER_TILE = (By.ID, 'modeCardLayout')

    def check_settings_availability(self):
        self.click_by_locator(self.SETTINGS_ICON)
        self.isSettingsAvailable = self.is_element_by_locator(self.SETTINGS_TITLE)
        self.click_back_android()
        return self.isSettingsAvailable

    def check_main_title(self):
        self.isMainTitleAvailable = False
        if self.is_element_by_locator(self.MAIN_TITLE):
            self.swipe_left_by_element(self.CUSTOMER_TILE)
            self.isMainTitleAvailable = self.is_element_by_locator(self.MAIN_TITLE)
        return self.isMainTitleAvailable

    def check_app_version(self):
        self.appVersion = self.get_element_text_by_locator(self.BUILD_NUMBER)
        return re.match(r'\d\.\d\.\d\.\d{3}', self.appVersion)

    def check_customer_description(self):
        self.isDescriptionAvailable = self.is_element_by_locator(self.CUSTOMER_DESCRIPTION)
        return self.isDescriptionAvailable


