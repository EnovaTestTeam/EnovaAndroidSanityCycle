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
    CREATE_MEETING_TOPICS = (By.ID, "com.harman.enova.beta:id/meetingTopicsLayout")
    CREATE_MEETING_TOPICS_LIST = (By.ID, "com.harman.enova.beta:id/topicItemCheckBox")
    CREATE_MEETING_ADD_TOPICS_BUTTON = (By.ID, "com.harman.enova.beta:id/addTopicButton")
    CREATE_MEETING_ADD_TOPICS_FORM = (By.ID, "com.harman.enova.beta:id/parentPanel")
    CREATE_MEETING_NEW_TOPICS_NAME_FIELD = (By.ID, "com.harman.enova.beta:id/topicText")
    CREATE_MEETING_NEW_TOPICS_FORM_OK_BUTTON = (By.ID, "android:id/button1")
    CREATE_MEETING_NEW_TOPICS_FORM_CANCEL_BUTTON = (By.ID, "android:id/button2")
    CREATE_MEETING_BUTTON = (By.ID, "com.harman.enova.beta:id/meetingCreateButton")
    MEETING_HEADER = (By.ID, "com.harman.enova.beta:id/meetingHeader")
    MEETING_EMPTY_SESSION_AREA = (By.ID, "com.harman.enova.beta:id/emptySessionLayout")
    MEETING_RECORD_BUTTON = (By.ID, "com.harman.enova.beta:id/recordBtn")
    MEETING_BACK_BUTTON = (By.ID, "com.harman.enova.beta:id/closeBtn")
    MEETING_DETAILS_BUTTON = (By.ID, "com.harman.enova.beta:id/detailsButton")
    MEETING_NAME = (By.ID, "com.harman.enova.beta:id/titleText")
    MEETING_EDIT_BUTTON = (By.ID, "com.harman.enova.beta:id/rightButton")
    MEETING_MARKERS_BUTTON = (By.ID, "com.harman.enova.beta:id/auxButton")
    MEETING_MARKERS_GROUP = (By.ID, "com.harman.enova.beta:id/markersGroup")

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

    def is_topics_on_create_meeting_page(self):
        return self.is_element_by_locator(self.CREATE_MEETING_TOPICS)

    def get_topics_list_create_meeting_page(self):
        return self.find_elements(self.CREATE_MEETING_TOPICS_LIST)

    def get_topic_name(self, topic):
        return self.get_element_text_by_element(topic)

    def click_add_topic_button(self):
        self.click_by_locator(self.CREATE_MEETING_ADD_TOPICS_BUTTON)

    def is_add_topic_form(self):
        return self.is_element_by_locator(self.CREATE_MEETING_ADD_TOPICS_FORM)

    def set_new_topic_name(self, name):
        self.send_keys_by_locator(self.CREATE_MEETING_NEW_TOPICS_NAME_FIELD, name)

    def click_ok_on_new_topic_form(self):
        self.click_by_locator(self.CREATE_MEETING_NEW_TOPICS_FORM_OK_BUTTON)

    def click_cancel_on_new_topic_form(self):
        self.click_by_locator(self.CREATE_MEETING_NEW_TOPICS_FORM_CANCEL_BUTTON)

    def add_new_topic(self, topic_name):
        self.click_add_topic_button()
        self.set_new_topic_name(topic_name)
        self.click_add_topic_button()

    def set_meeting_name(self, meeting_name):
        self.clear_element_by_locator(self.CREATE_MEETING_NAME_TEXT)
        self.send_keys_by_locator(self.CREATE_MEETING_NAME_TEXT, meeting_name)

    def click_create_meeting_button(self):
        self.click_by_locator(self.CREATE_MEETING_BUTTON)

    def create_new_meeting(self, meeting_name=None):
        self.open_create_meeting_page()
        if meeting_name:
            self.set_meeting_name(meeting_name)
        self.swipe_top()
        self.click_create_meeting_button()

    def is_meeting_created(self):
        if self.is_element_by_locator(self.MEETING_HEADER) and \
                self.is_element_by_locator(self.MEETING_EMPTY_SESSION_AREA) and \
                self.is_element_by_locator(self.MEETING_RECORD_BUTTON):
            return True
        else:
            return False

    def get_meeting_name(self):
        return self.get_element_text_by_locator(self.MEETING_NAME)

    def is_meeting_edit_button(self):
        return self.is_element_by_locator(self.MEETING_EDIT_BUTTON)

    def open_meeting_edit_page(self):
        self.click_by_locator(self.MEETING_EDIT_BUTTON)

    def is_meeting_edit_page(self):
        if self.is_element_by_locator(self.CREATE_MEETING_HEADER) and self.get_element_text_by_locator(self.CREATE_MEETING_HEADER_TEXT) == "Update Meeting":
            return True
        else:
            return False

    def is_meeting_markers_button(self):
        return self.is_element_by_locator(self.MEETING_MARKERS_BUTTON)

    def open_meeting_markers(self):
        self.click_by_locator(self.MEETING_MARKERS_BUTTON)

    def is_meeting_markers_form(self):
        return self.is_element_by_locator(self.MEETING_MARKERS_GROUP)
