from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class MeetingPage(BasePage):
    MEETING_BUTTON = (By.ID, "com.harman.enova.beta:id/meetingButton")

    def __init__(self, driver):
        super().__init__(driver)


