import allure
import pytest
import re
from allure_commons.types import AttachmentType

from Pages.WelcomeScreen import WelcomeScreen
from Pages.LoginPage import LoginPage
from Pages.ChooseCustomersScreen import ChooseCustomerScreen
from TestData.config import TestData
from Pages.SettingsPage import SettingsInApp
from Pages.EnovaChatPage import EnovaChatPage
from Pages.MeetingPage import MeetingPage


@pytest.mark.usefixtures("login")
class TestEnovaApp:

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

    """Welcome screen overview test"""

    @pytest.mark.skip
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
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

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
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
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
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
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
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

        with allure.step("Check that 'Email' field is empty and after click 'Submit' button "
                         "messsage about invalid email is displayed"):
            self.login_page.click_send_button()
            assert self.login_page.is_warning_red_text()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

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
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    """Create meetings: meeting creation window is opened"""

    @pytest.mark.skip
    @allure.description("Opening meeting creation page")
    def test_open_create_meeting_page(self):
        self.meetings = MeetingPage(self.driver)
        with allure.step("Open 'Create meeting' page"):
            self.meetings.open_create_meeting_page()
        with allure.step("Check that 'Create meeting' page is opened"):
            assert self.meetings.is_create_meeting_page(), \
                "'Create meeting' page is not opened or page header is incorrect"
        with allure.step("Check 'Create meeting' header text"):
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            assert self.meetings.get_meeting_create_header_text() == "New Meeting" or self.meetings.get_meeting_create_header_text() == "Новое совещание", \
                "Incorrect header text on 'Create meeting' page"

    """Create meetings: meetings name is presented"""

    @pytest.mark.skip
    @allure.description("Check meeting name on 'Create meeting' page")
    def test_meeting_name_on_create_meeting_page(self):
        self.meetings = MeetingPage(self.driver)
        with allure.step("Open 'Create meeting' page"):
            self.meetings.open_create_meeting_page()

        with allure.step("Check that meeting name is presented on Create meeting page"):
            assert self.meetings.is_meeting_name_on_create_meeting_page(), \
                "Meeting name field is not presented on 'Create meeting' page "
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

        with allure.step("Check meeting name on 'Create meeting' page"):
            # current_datetime = str(datetime.now()).split(" ")
            # time = current_datetime[1].split(".")[0]
            # data = current_datetime[0].split("-")
            assert re.match(TestData.MEETING_NAME_REG, self.meetings.get_meeting_name_create_meeting_page()), \
                "Format meeting name on Create meeting page is incorrect"

    """Create meetings: Topics are presented"""

    @pytest.mark.skip
    @allure.description("Check topics on 'Create meeting' page")
    def test_tags_on_create_meeting_page(self):
        self.meetings = MeetingPage(self.driver)
        with allure.step("Open 'Create meeting' page"):
            self.meetings.open_create_meeting_page()

        with allure.step("Check that topics are presented on Create meeting page"):
            assert self.meetings.is_topics_on_create_meeting_page(), \
                "Topics area is not presented on 'Create meeting' page"
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            assert len(self.meetings.get_topics_list_create_meeting_page()) > 0, \
                "Topics are not present on 'Create meeting' page"

    """Create meetings: add topic"""

    @pytest.mark.skip
    @allure.description("Add new topic on 'Create meeting' page")
    def test_add_new_topic_on_create_meeting_page(self):
        self.meetings = MeetingPage(self.driver)
        new_topic_name = "New topic"
        with allure.step("Open 'Create meeting' page"):
            self.meetings.open_create_meeting_page()
            topics_list = self.meetings.get_topics_list_create_meeting_page()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Click 'Add topic' button"):
            self.meetings.click_add_topic_button()
        with allure.step(f"Set new topic name: {new_topic_name}"):
            self.meetings.set_new_topic_name(new_topic_name)
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Click 'OK' button"):
            self.meetings.click_ok_on_new_topic_form()
        with allure.step(f"Check that new topic '{new_topic_name}' is added"):
            new_topic_list = self.meetings.get_topics_list_create_meeting_page()
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            assert len(new_topic_list) == len(topics_list)+1, \
                "Meetings list is incorrect after adding new topic"
        with allure.step("Check that added topic is 'New topic'"):
            assert self.meetings.get_topic_name(new_topic_list[-1]) == new_topic_name, \
                "Name of added topic is incorrect"

    """Create new meeting"""

    @pytest.mark.skip
    @allure.description("Create new meeting test")
    def test_create_new_meeting(self):
        self.meetings = MeetingPage(self.driver)
        with allure.step("Create new meeting with default name and without topics"):
            self.meetings.create_new_meeting()

        with allure.step("Check that meeting is created and contains name, text area and mic button"):
            assert self.meetings.is_meeting_created(), \
                "Meeting is not created or created incorrectly"
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Check name of created meeting"):
            assert re.match(TestData.MEETING_NAME_REG, self.meetings.get_meeting_name()), \
                "Format of meeting name is incorrect"

    """Meeting screen: meeting name"""

    @pytest.mark.skip
    @pytest.mark.parametrize("meeting_name", [
        "New meeting",
        "Новый митинг",
        "!@#$%$%^^",
    ])
    @allure.description("Create meeting with different format of names and check name")
    def test_new_meeting_name(self, meeting_name):
        self.meetings = MeetingPage(self.driver)
        with allure.step(f"Create new meeting with name: {meeting_name}"):
            self.meetings.create_new_meeting(meeting_name)
        with allure.step("Check that meeting is created and contains name, text area and mic button"):
            assert self.meetings.is_meeting_created(), \
                "Meeting is not created or created incorrectly"
        with allure.step("Check name of created meeting"):
            assert self.meetings.get_meeting_name() == meeting_name, \
                f"Name of created meeting is not {meeting_name}"
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    """Meeting screen: edit meeting button"""

    @pytest.mark.skip
    @allure.description("Check that Edit button is present for meeting and Edit window can be opened")
    def test_edit_meeting_button(self):
        self.meetings = MeetingPage(self.driver)
        with allure.step("Create new meeting"):
            self.meetings.create_new_meeting()

        with allure.step("Check that 'Edit' button is present on Meeting page"):
            assert self.meetings.is_meeting_edit_button(), \
                "'Edit' button is not found on Meeting page"

        with allure.step("Open 'Edit meeting' page"):
            self.meetings.open_meeting_edit_page()

        with allure.step("Check that 'Edit meeting' page is opened"):
            assert self.meetings.is_meeting_edit_page(), \
                "'Edit meeting' page is not opened or page header is incorrect"
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    """Meeting screen: meeting markers button"""

    @pytest.mark.skip
    @allure.description("Check that Markers button is present for meeting and markers form can be opened")
    def test_markers_meeting_button(self):
        self.meetings = MeetingPage(self.driver)
        with allure.step("Create new meeting"):
            self.meetings.create_new_meeting()

        with allure.step("Check that 'Markers' button is present on Meeting page"):
            assert self.meetings.is_meeting_markers_button(), \
                "'Markers' button is not found on Meeting page"

        with allure.step("Open markers for meeting"):
            self.meetings.open_meeting_markers()

        with allure.step("Check that markers form is opened"):
            assert self.meetings.is_meeting_markers_form(), \
                "Markers for is not opened or for doesn't contain list of markers"
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    """Meeting screen: meeting details button"""

    @pytest.mark.skip
    @allure.description("Check that Details button is present for meeting and is disabled for empty meeting")
    def test_markers_meeting_button(self):
        self.meetings = MeetingPage(self.driver)
        with allure.step("Create new meeting"):
            self.meetings.create_new_meeting()

        with allure.step("Check that 'Details' button is present on Meeting page"):
            assert self.meetings.is_meeting_details_button(), \
                "'Details' button is not found on Meeting page"

        with allure.step("Check that 'Details' button is disabled for empty meeting"):
            assert not self.meetings.is_enabled_meeting_details_button(), \
                "'Details' button is enabled for empty meeting"
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    """Change meeting name"""

    @pytest.mark.skip
    @allure.description("Changing meeting name test")
    @pytest.mark.parametrize("new_name", [
        "New meeting",
        "Новый митинг",
        "!@#$%$%^^",
    ])
    def test_change_meeting_name(self, new_name):
        self.meetings = MeetingPage(self.driver)
        with allure.step("Create new meeting"):
            self.meetings.create_new_meeting()
        with allure.step("Open 'Edit meeting' page"):
            self.meetings.open_meeting_edit_page()
        with allure.step("Change meeting name"):
            self.meetings.set_meeting_name(new_name)
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Save changes in meeting"):
            self.meetings.save_changes_in_meeting()

        with allure.step("Check new meeting name"):
            assert self.meetings.get_meeting_name() == new_name, \
                f"Name of created meeting is not {new_name}"
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    """Change meeting topics"""

    @pytest.mark.skip
    @allure.description("Changing meeting topics test")
    def test_change_meeting_topics(self):
        self.meetings = MeetingPage(self.driver)
        with allure.step("Create new meeting"):
            self.meetings.create_new_meeting()
        with allure.step("Open 'Edit meeting' page"):
            self.meetings.open_meeting_edit_page()
        with allure.step("Select all topics"):
            self.meetings.select_all_topics()
        selected_topics = self.meetings.get_names_selected_topics()
        with allure.step("Save changes in meeting"):
            self.meetings.save_changes_in_meeting()
        new_topics = self.meetings.get_meeting_topics_list()
        with allure.step("Check that topics are added in meeting"):
            assert selected_topics == new_topics, "Topics list after editing is incorrect"
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    """Meeting recording audio"""

    @allure.description("Meeting recording audio test")
    @pytest.mark.parametrize("audio_path", [
        "New meeting",
        "Новый митинг",
        "!@#$%$%^^",
    ])
    def test_record_meeting(self, audio_path):
        self.meetings = MeetingPage(self.driver)
        with allure.step("Create new meeting"):
            self.meetings.create_new_meeting()

