from Pages.SettingsPage import SettingsInApp


class SettingsActions(SettingsInApp):
    def __init__(self, driver):
        super().__init__(driver)

    def set_settings_for_wer_test(self, pauseDetectionTimeoutLayout):
        self.set_common_pause_timeout(pauseDetectionTimeoutLayout)
        self.set_common_transcribe_turnon()