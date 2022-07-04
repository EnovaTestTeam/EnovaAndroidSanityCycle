import allure
import pytest

from Pages.WelcomeScreen import WelcomeScreen
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Pages.ChooseCustomersScreen import ChooseCustomerScreen
from TestData.config import TestData
from Pages.SettingsPage import SettingsInApp
from Pages.EnovaChatPage import EnovaChatPage
from Pages.MeetingPage import MeetingPage


#@pytest.mark.parametrize("login_data", [TestData.LOGIN_DATA])
class TestEnovaApp(BaseTest):

    """Registering device test"""

    # @pytest.mark.parametrize("login_data", [TestData.LOGIN_DATA])
    # def test_login(self, login_data):
    #     self.login_page = LoginPage(self.driver)
    #     self.settings = SettingsInApp(self.driver)
    #     self.customers_page = ChooseCustomerScreen(self.driver)
    #
    #     self.login_page.login(login_data["SERVER"], login_data["USER_NAME"])
    #
    #     flag = self.customers_page.is_choose_customer_page()
    #     assert flag
    #
    #     server_name = self.settings.get_server()
    #     assert server_name == login_data["SERVER"]

    """Welcome screen owerview test"""

    @allure.description("TEST: Welcome screen overview")
    def test_welcome_screen(self):
        print("Test_WelcomeScreen")
        self.welcome_screen = WelcomeScreen(self.driver)
        assert self.welcome_screen.check_settings_availability()
        assert self.welcome_screen.check_app_version()
        assert self.welcome_screen.check_customer_description()
        assert self.welcome_screen.check_main_title()

    """Privacy Policy checking test"""

    @pytest.mark.skip
    @allure.description("Privacy Policy checking test")
    def test_privacy_policy(self):
        self.settings = SettingsInApp(self.driver)
        self.customers_page = ChooseCustomerScreen(self.driver)

        with allure.step("Open Privacy Policy"):
            self.settings.open_privacy_policy()

        with allure.step("Check that Privacy Policy page is opened"):
            assert self.settings.is_privacy_policy()

        with allure.step("Close Privacy Policy page"):
            self.settings.close_privacy_policy()

    """Show metrics test"""

    @pytest.mark.skip
    @allure.description("Show metrics test")
    def test_show_metrics(self):
        self.settings = SettingsInApp(self.driver)
        self.customers_page = ChooseCustomerScreen(self.driver)
        self.enova_chat = EnovaChatPage(self.driver)

        with allure.step("Switch on 'Show metrics' option in Settings"):
            self.settings.show_metrix_switch_on()
        with allure.step("Open chat for Enova customer"):
            self.customers_page.open_chatmode_for_customer("Enova")
        with allure.step("Make request in chat"):
            self.enova_chat.send_question_in_chat_not_dialog(r"C:\Users\ruvkuminov\TestsAutomation\EnovaAndroidTests\TestData\AudioData\what_time_is_it.mp3")

        with allure.step("Check that metrics are displayed in chat under system answer"):
            assert self.enova_chat.is_metrics_in_chat(), "Metrics is not present in chat after"
        with allure.step("Check that metrics contained not empty data"):
            assert self.enova_chat.is_data_in_metrix(), "Metrics are empty, no data is in metrics"

    """Show versions components test"""

    @pytest.mark.skip
    @allure.description("Show versions components test")
    def test_show_versions(self):
        self.settings = SettingsInApp(self.driver)
        self.customers_page = ChooseCustomerScreen(self.driver)
        self.enova_chat = EnovaChatPage(self.driver)

        with allure.step("Switch on 'Show versions' option in Settings"):
            self.settings.show_versions_switch_on()
        with allure.step("Open chat for Enova customer"):
            self.customers_page.open_chatmode_for_customer("Enova")
        with allure.step("Make request in chat"):
            self.enova_chat.send_question_in_chat_not_dialog(
                r"C:\Users\ruvkuminov\TestsAutomation\EnovaAndroidTests\TestData\AudioData\what_time_is_it.mp3")

        with allure.step("Check that metrics are displayed in chat under system answer"):
            assert self.enova_chat.is_versions_in_chat(), "Metrics is not present in chat after"
        with allure.step("Check that metrics contained not empty data"):
            assert self.enova_chat.is_data_in_versions(), "Metrics are empty, no data is in metrics"

    """Unregistering device test"""

    @pytest.mark.skip
    @allure.description("Unregistering device test")
    def test_logout(self):
        self.login_page = LoginPage(self.driver)
        self.settings = SettingsInApp(self.driver)
        self.customers_page = ChooseCustomerScreen(self.driver)

        with allure.step("Open Settings -> Device page and click 'Unregister' button"):
            self.settings.unregister_device()

        with allure.step("Check that login page is opened"):
            assert self.login_page.is_login_page()

        with allure.step("Check that 'Email' field is empty and after click 'Submit' button "
                         "messsage about invalid email is displayed"):
            self.login_page.click_send_button()
        assert self.login_page.is_warning_red_text()

    """Meetings button is present in Enova chat"""

    @pytest.mark.skip
    @allure.description("Meetings button is present in Enova chat test")
    def test_meeting_button_present(self):
        self.customers_page = ChooseCustomerScreen(self.driver)
        self.enova_chat = EnovaChatPage(self.driver)

        with allure.step("Open Enova chat"):
            self.customers_page.open_chatmode_for_customer("Enova")
        with allure.step("Check that meeting button is present in chat"):
            assert self.enova_chat.is_meeting_button()

    """Create meetings: meeting creation window is opened"""

    @allure.description("Opening meeting creation page")
    def test_open_create_meeting_page(self):
        self.meetings = MeetingPage(self.driver)
        with allure.step("Open 'Create meeting' page"):
            self.meetings.open_create_meeting_page()

        with allure.step("Check that 'Create meeting' page is opened"):
            assert self.meetings.is_create_meeting_page(), \
                "'Create meeting page is not opened or page header is incorrect'"
        with allure.step("Check 'Create meeting' header text"):
            assert self.meetings.get_meeting_create_header_text() == "New Meeting" or self.meetings.get_meeting_create_header_text() == "Новое совещание", \
                "Incorrect header text on 'Create meeting' page"

    """Create meetings: meetings name is presented"""

    @allure.description("Check meeting name on 'Create meeting' page")
    def test_open_create_meeting_page(self):
        self.meetings = MeetingPage(self.driver)
        with allure.step("Open 'Create meeting' page"):
            self.meetings.open_create_meeting_page()

        with allure.step("Check that 'Create meeting' page is opened"):
            assert self.meetings.is_create_meeting_page(), \
                "'Create meeting page is not opened or page header is incorrect'"
        with allure.step("Check 'Create meeting' header text"):
            assert self.meetings.get_meeting_create_header_text() == "New Meeting" or self.meetings.get_meeting_create_header_text() == "Новое совещание", \
                "Incorrect header text on 'Create meeting' page"

    """Create meetings: Tags are presented"""
    """Create meetings: add tag"""
    """Create new meeting"""
    """Meeting screen: meeting name"""
    """Meeting screen: edit meeting button"""
    """Meeting screen: meeting markers button"""
    """Veeting screen: meeting statistic button"""
    """Change meeting name"""
    """Change meeting tags"""
    """Meeting recording: short audio"""
    """Meeting recording: middle audio audio"""
    """Meeting recording: long audio audio"""
