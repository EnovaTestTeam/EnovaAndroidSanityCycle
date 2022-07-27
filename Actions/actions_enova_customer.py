from Pages.ChooseCustomersScreen import ChooseCustomerScreen
from Pages.EnovaChatPage import EnovaChatPage
from Pages.SettingsPage import SettingsInApp


class EnovaActions:

    def __init__(self, driver):
        self.driver = driver

    def make_request_enova_chat(self, audio_path, mode):
        settings = SettingsInApp(self.driver)
        customers_page = ChooseCustomerScreen(self.driver)
        enova_chat = EnovaChatPage(self.driver)

        customers_page.open_chatmode_for_customer("Enova")
        enova_chat.select_mode(mode)
        enova_chat.send_question_in_chat_not_dialog(audio_path)
