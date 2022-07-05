from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Pages.ChooseCustomersScreen import ChooseCustomerScreen
from Pages.EnovaChatPage import EnovaChatPage


class MeetingPage(BasePage):
    MEETING_BUTTON = (By.ID, "com.harman.enova.beta:id/meetingButton")
    CREATE_MEETING_HEADER = (By.ID, "com.harman.enova.beta:id/meetingCreateHeader")
    CREATE_MEETING_HEADER_TEXT = (By.ID, "com.harman.enova.beta:id/titleText")
    CREATE_MEETING_NAME = (By.ID, "com.harman.enova.beta:id/meetingTitleLayout")
    CREATE_MEETING_NAME_TEXT = (By.ID, "com.harman.enova.beta:id/meetingNameEditText")

    def __init__(self, driver):
        super().__init__(driver)

    def open_create_meeting_page(self):
        self.customers_page = ChooseCustomerScreen(self.driver)
        self.enova_chat = EnovaChatPage(self.driver)
        self.customers_page.open_enova_chat()
        self.click_by_locator(self.MEETING_BUTTON)

    def is_create_meeting_page(self):
        return self.is_element_by_locator(self.CREATE_MEETING_HEADER)

    def get_meeting_create_header_text(self):
        return self.get_element_text_by_locator(self.CREATE_MEETING_HEADER_TEXT)

    def is_meeting_name_on_create_meeting_page(self):
        return self.is_element_by_locator(self.CREATE_MEETING_NAME)

    def get_meeting_name_create_meeting_page(self):
        return self.get_element_text_by_locator(self.CREATE_MEETING_NAME_TEXT)


