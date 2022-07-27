from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class EnovaChatPage(BasePage):
    SKIP_TUTORIAL_BUTTON = (By.ID, "com.harman.enova.beta:id/skipButton")
    MIC_BUTTON = (By.ID, "com.harman.enova.beta:id/recordBtn")
    LISTENING_STATE_BUTTON = (By.ID, "com.harman.enova.beta:id/listeningView")
    SERVER_PROCESSING_BUTTON = (By.ID, "com.harman.enova.beta:id/processingView")
    CHAT_BACK_BUTTON = (By.ID, "com.harman.enova.beta:id/closeBtn")
    CHAT_TEXT = (By.ID, "com.harman.enova.beta:id/requestTextView")
    METRICS = (By.ID, "com.harman.enova.beta:id/metricsLayout")
    METRICS_TEXT = (By.ID, "com.harman.enova.beta:id/metricsTextView")
    VERSIONS = (By.ID, "com.harman.enova.beta:id/componentVersionsLayout")
    VERSIONS_TEXT = (By.ID, "com.harman.enova.beta:id/versionTextView")
    MEETING_BUTTON = (By.ID, "com.harman.enova.beta:id/meetingButton")
    WUW_TEXT = (By.ID, "com.harman.enova.beta:id/welcome_message")
    MENU_BUTTON = (By.ID, "com.harman.enova.beta:id/menuButton")
    MENU_LIST = (By.ID, "com.harman.enova.beta:id/title")
    MODES_LIST = (By.ID, "com.harman.enova.beta:id/modeName")
    ANSWER = (By.ID, "com.harman.enova.beta:id/responseLayout")
    ANSWER_TEXT = (By.ID, "com.harman.enova.beta:id/responseTextView")
    IMAGE_CONTENT = (By.ID, "com.harman.enova.beta:id/contentImageView")
    TEXT_CONTENT = (By.CLASS_NAME, "android.view.View")

    def __init__(self, driver):
        super().__init__(driver)

    def skip_tutorial(self):
        self.click_by_locator(self.SKIP_TUTORIAL_BUTTON)

    def listening_mode_on(self):
        self.click_by_locator(self.MIC_BUTTON)

    def is_listening_mode_on(self):
        if self.is_element_by_locator(self.LISTENING_STATE_BUTTON):
            return True
        else:
            return False

    def is_listening_mode_off(self):
        if self.is_element_by_locator(self.MIC_BUTTON):
            return True
        else:
            return False

    def is_server_processing_state(self):
        if self.is_element_by_locator(self.SERVER_PROCESSING_BUTTON):
            return True
        else:
            return False

    def is_metrics_in_chat(self):
        if self.is_element_by_locator(self.METRICS):
            return True
        else:
            return False

    def get_metrics_text(self):
        if self.is_metrics_in_chat():
            return self.get_element_text_by_locator(self.METRICS_TEXT)
        else:
            return None

    def is_data_in_metrix(self):
        metrics_text = self.get_metrics_text().split(",")
        metrix = dict()
        for m in metrics_text:
            temp = [m.split("=")]
            metrix[temp[0][0]] = temp[0][1]
        if None not in metrix.values() and "" not in metrix.values():
            return True
        else:
            return False

    def is_versions_in_chat(self):
        if self.is_element_by_locator(self.VERSIONS):
            return True
        else:
            return False

    def get_versions_text(self):
        if self.is_versions_in_chat():
            return self.get_element_text_by_locator(self.VERSIONS_TEXT)
        else:
            return None

    def is_data_in_versions(self):
        versions_text = self.get_versions_text().split(r"\n")
        versions = dict()
        for m in versions_text:
            temp = [m.split("=")]
            versions[temp[0][0]] = temp[0][1]
        if None not in versions.values() and "" not in versions.values():
            return True
        else:
            return False

    def exit_from_chatmode(self):
        self.click_by_locator(self.CHAT_BACK_BUTTON)

    def send_question_in_chat_not_dialog(self, audio_path):
        self.listening_mode_on()
        self.play(audio_path)
        self.is_listening_mode_off()

    def say_in_enova_chat(self, audio_path):
        if self.is_listening_mode_off():
            self.play(audio_path)

    def get_answer_from_chat(self):
        return self.get_element_text_by_locator(self.ANSWER_TEXT)

    def is_answer_in_chat(self):
        return self.find_element(self.ANSWER)

    def is_meeting_button(self):
        return self.is_element_by_locator(self.MEETING_BUTTON)

    def is_wuw_text(self):
        return self.is_element_by_locator(self.WUW_TEXT)

    def get_wuw_text(self):
        return self.get_element_text_by_locator(self.WUW_TEXT)

    def select_mode(self, mode_title):
        self.click_by_locator(self.MENU_BUTTON)
        menu_items = self.find_elements(self.MENU_LIST)
        for item in menu_items:
            if self.get_element_text_by_element(item) == "Select Mode" or self.get_element_text_by_element(item) == "Выберите режим":
                self.click_by_element(item)
                break
        modes = self.find_elements(self.MODES_LIST)
        for mode in modes:
            if self.get_element_text_by_element(mode) == mode_title:
                self.click_by_element(mode)
                break

    def is_image_content(self):
        return self.is_element_by_locator(self.IMAGE_CONTENT)

    def is_text_content(self):
        return self.is_element_by_locator(self.TEXT_CONTENT)

    def get_text_from_text_content(self):
        return self.get_element_text_by_locator(self.TEXT_CONTENT)


