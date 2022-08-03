import time
from numpy import zeros, uint8

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
    MEETING_RECORDING_BUTTON = (By.ID, "com.harman.enova.beta:id/recordBtn")
    MEETING_LISTENING_VIEW_BUTTON = (By.ID, "com.harman.enova.beta:id/listeningView")
    MEETING_BACK_BUTTON = (By.ID, "com.harman.enova.beta:id/closeBtn")
    MEETING_DETAILS_BUTTON = (By.ID, "com.harman.enova.beta:id/detailsButton")
    MEETING_NAME = (By.ID, "com.harman.enova.beta:id/titleText")
    MEETING_EDIT_BUTTON = (By.ID, "com.harman.enova.beta:id/rightButton")
    MEETING_MARKERS_BUTTON = (By.ID, "com.harman.enova.beta:id/auxButton")
    MEETING_MARKERS_GROUP = (By.ID, "com.harman.enova.beta:id/markersGroup")
    MEETING_TOPICS_LIST = (By.ID, "com.harman.enova.beta:id/chip")
    MEETING_RECORDING_TIME = (By.ID, "com.harman.enova.beta:id/meetingTimeView")
    MEETING_RECORDING_ANIMATION = (By.ID, "com.harman.enova.beta:id/waveformView")
    MEETING_TEXT = (By.ID, "com.harman.enova.beta:id/contentText")
    MEETING_DETAILS_LIST = (By.ID, "android:id/title")
    MEETING_DETAILS_HEADER_TEXT = (By.ID, "com.harman.enova.beta:id/titleText")
    MEETING_SUBTITLES_TEXT = (By.ID, "com.harman.enova.beta:id/contentText")
    BACK_BUTTON_FOR_DETAILS = (By.ID, "com.harman.enova.beta:id/backButton")
    SPEAKERS_LIST = (By.ID, "com.harman.enova.beta:id/meetingSpeaker")

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

    def select_all_topics(self):
        topics_list = self.find_elements(self.CREATE_MEETING_TOPICS_LIST)
        for topic in topics_list:
            self.click_by_element(topic)

    def get_names_selected_topics(self):
        selected_topics = []
        topics_list = self.find_elements(self.CREATE_MEETING_TOPICS_LIST)
        for topic in topics_list:
            if self.is_element_checked_by_element(topic):
                selected_topics.append(self.get_element_text_by_element(topic))
        return selected_topics

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
                self.is_element_by_locator(self.MEETING_RECORDING_BUTTON):
            return True
        else:
            return False

    def get_meeting_name(self):
        return self.get_element_text_by_locator(self.MEETING_NAME)

    def get_meeting_topics_list(self):
        topics = self.find_elements(self.MEETING_TOPICS_LIST)
        topics_names = []
        for topic in topics:
            topics_names.append(self.get_element_text_by_element(topic))
        return topics_names

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

    def is_meeting_details_button(self):
        return self.is_element_by_locator(self.MEETING_DETAILS_BUTTON)

    def open_meeting_details(self):
        self.click_by_locator(self.MEETING_DETAILS_BUTTON)

    def is_meeting_details_form(self):
        return self.is_element_by_locator(self.MEETING_MARKERS_GROUP)

    def is_enabled_meeting_details_button(self):
        return self.is_element_enabled_by_locator(self.MEETING_DETAILS_BUTTON)

    def save_changes_in_meeting(self):
        self.swipe_top()
        self.click_create_meeting_button()

    def start_recording_meeting(self):
        self.click_by_locator(self.MEETING_RECORDING_BUTTON)

    def is_meeting_in_listening_state(self):
        return self.is_element_by_locator(self.MEETING_LISTENING_VIEW_BUTTON)

    def stop_recording_meeting(self):
        self.click_by_locator(self.MEETING_LISTENING_VIEW_BUTTON)
        self.find_element(self.MEETING_RECORDING_BUTTON)

    def is_meeting_recording_timer(self):
        return self.is_element_by_locator(self.MEETING_RECORDING_TIME)

    def is_meeting_recording_animation(self):
        return self.is_element_by_locator(self.MEETING_RECORDING_ANIMATION)

    def record_meeting(self, audio_path):
        start_time = time.time()
        self.start_recording_meeting()
        self.play(audio_path)
        self.pause(2)
        recording_time = time.time() - start_time
        self.stop_recording_meeting()
        return recording_time


    def is_enabled_meeting_recording_button(self):
        return self.is_element_enabled_by_locator(self.MEETING_RECORDING_BUTTON)

    def is_empty_session_meeting(self):
        return self.is_element_by_locator(self.MEETING_EMPTY_SESSION_AREA)

    def is_meeting_time(self):
        return self.is_element_by_locator(self.MEETING_RECORDING_TIME)

    def get_meeting_time(self):
        return self.get_element_text_by_locator(self.MEETING_RECORDING_TIME)

    def is_meeting_text(self):
        return self.is_element_by_locator(self.MEETING_TEXT)

    def get_meeting_text(self):
        text = []
        elements = []
        flag = True
        while flag:
            flag = False
            temp = self.find_elements(self.MEETING_TEXT)
            for element in temp:
                if element not in elements:
                    flag = True
                    elements.append(element)
                    text.append(self.get_element_text_by_element(element))
            self.swipe_meeting()
        return text

    def open_meeting_detais(self):
        self.click_by_locator(self.MEETING_DETAILS_BUTTON)

    def get_details_list(self):
        details = []
        details_list = self.find_elements(self.MEETING_DETAILS_LIST)
        for d in details_list:
            details.append(self.get_element_text_by_element(d))
        return details

    def open_meeting_subtitles(self):
        details_list = self.find_elements(self.MEETING_DETAILS_LIST)
        for d in details_list:
            if self.get_element_text_by_element(d) == "Subtitles" or self.get_element_text_by_element(d) == "Субтитры":
                self.click_by_element(d)
                break

    def is_meeting_subtitles_page(self):
        if self.get_element_text_by_locator(self.MEETING_DETAILS_HEADER_TEXT) == "Meeting Subtitles" \
                or self.get_element_text_by_locator(self.MEETING_DETAILS_HEADER_TEXT) == "Субтитры совещания":
            return True
        else:
            return False

    def get_meeting_subtitles(self):
        return self.get_element_text_by_locator(self.MEETING_SUBTITLES_TEXT)

    def pars_subtitles(self, text):
        text = text.split('\n')
        temp = []
        for s in text:
            if len(s) > 1 and ("[" in s or "]" in s):
                temp.append(s.split("]")[-1])
        return " ".join(temp)

    def get_meeting_recording_time(self):
        return self.get_element_text_by_locator(self.MEETING_RECORDING_TIME)

    def back_to_meeting_from_details(self):
        self.click_by_locator(self.BACK_BUTTON_FOR_DETAILS)

    def is_speakers(self):
        return self.is_element_by_locator(self.SPEAKERS_LIST)

    def get_speakers_list(self):
        speakers_list = []
        speakers_elements = self.find_elements(self.SPEAKERS_LIST)
        for speaker in speakers_elements:
            speakers_list.append(self.get_element_text_by_element(speaker))
        return speakers_list

    def wer(self, r, h):
        if not r:
            if not h:
                return 100.0
            else:
                return 0.0
        if not h:
            return 100.0

        r = r.split(' ')
        h = h.split(' ')
        d = zeros((len(r) + 1) * (len(h) + 1), dtype=uint8)
        d = d.reshape((len(r) + 1, len(h) + 1))

        for i in range(len(r) + 1):
            d[i][0] = i

        for j in range(len(h) + 1):
            d[0][j] = j

        for i in range(1, len(r) + 1):
            for j in range(1, len(h) + 1):
                if r[i - 1] == h[j - 1]:
                    d[i][j] = d[i - 1][j - 1]
                else:
                    substitution = d[i - 1][j - 1] + 1
                    insertion = d[i][j - 1] + 1
                    deletion = d[i - 1][j] + 1
                    d[i][j] = min(substitution, insertion, deletion)

        return d[len(r)][len(h)] / len(r) * 100
