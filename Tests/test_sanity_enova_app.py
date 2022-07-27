import allure
import pytest
import re
import time
from allure_commons.types import AttachmentType

from Actions.actions_enova_customer import EnovaActions
from Pages.WelcomeScreen import WelcomeScreen
from Pages.LoginPage import LoginPage
from Pages.ChooseCustomersScreen import ChooseCustomerScreen
from TestData.config import TestData
from Pages.SettingsPage import SettingsInApp
from Pages.EnovaChatPage import EnovaChatPage
from Pages.MeetingPage import MeetingPage


@pytest.mark.parametrize("server, user, protocol, language", [
    ("US West", "tbd@gmail.com", "WebSocket", "English"),
    #("US West", "tbd@gmail.com", "HTTPS", "English"),
    #("US West", "tbd@gmail.com", "WebSocket", "Russian"),
    #("US West", "tbd@gmail.com", "HTTPS", "Russian"),
])
class TestEnovaApp:
    """Registering device test"""

    # def test_login(self, driver, server, user, protocol, language):
    #     self.login_page = LoginPage(driver)
    #     self.settings = SettingsInApp(driver)
    #     self.customers_page = ChooseCustomerScreen(driver)
    #
    #     self.login_page.login(server, user)
    #
    #     flag = self.customers_page.is_choose_customer_page()
    #     assert flag
    #
    #     server_name = self.settings.get_server()
    #     assert server_name == server

    """Welcome screen overview test"""

    @pytest.mark.skip
    @allure.description("TEST: Welcome screen overview")
    def test_welcome_screen(self, driver, login, server, user, protocol, language):
        print("Test_WelcomeScreen")
        self.welcome_screen = WelcomeScreen(driver)
        assert self.welcome_screen.check_settings_availability()
        assert self.welcome_screen.check_app_version()
        assert self.welcome_screen.check_customer_description()
        assert self.welcome_screen.check_main_title()

    """Privacy Policy checking test"""

    @pytest.mark.skip
    @allure.description("Privacy Policy checking test")
    def test_privacy_policy(self, driver, login, server, user, protocol, language):
        self.settings = SettingsInApp(driver)
        self.customers_page = ChooseCustomerScreen(driver)

        with allure.step("Open Privacy Policy"):
            self.settings.open_privacy_policy()

        with allure.step("Check that Privacy Policy page is opened"):
            assert self.settings.is_privacy_policy()
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

        with allure.step("Close Privacy Policy page"):
            self.settings.close_privacy_policy()

    """Show metrics test"""

    @pytest.mark.skip
    @allure.description("Show metrics test")
    def test_show_metrics(self, driver, login, server, user, protocol, language):
        self.settings = SettingsInApp(driver)
        self.customers_page = ChooseCustomerScreen(driver)
        self.enova_chat = EnovaChatPage(driver)

        with allure.step("Switch on 'Show metrics' option in Settings"):
            self.settings.show_metrix_switch_on()
        with allure.step("Open chat for Enova customer"):
            self.customers_page.open_chatmode_for_customer("Enova")
        with allure.step("Make request in chat"):
            self.enova_chat.send_question_in_chat_not_dialog(TestData.AUDIO_FOR_SINGLE_INTENTS[0][0])

        with allure.step("Check that metrics are displayed in chat under system answer"):
            assert self.enova_chat.is_metrics_in_chat(), "Metrics is not present in chat after"
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Check that metrics contained not empty data"):
            assert self.enova_chat.is_data_in_metrix(), "Metrics are empty, no data is in metrics"

    """Show versions components test"""

    @pytest.mark.skip
    @allure.description("Show versions components test")
    def test_show_versions(self, driver, login, server, user, protocol, language):
        self.settings = SettingsInApp(driver)
        self.customers_page = ChooseCustomerScreen(driver)
        self.enova_chat = EnovaChatPage(driver)

        with allure.step("Switch on 'Show versions' option in Settings"):
            self.settings.show_versions_switch_on()
        with allure.step("Open chat for Enova customer"):
            self.customers_page.open_chatmode_for_customer("Enova")
        with allure.step("Make request in chat"):
            self.enova_chat.send_question_in_chat_not_dialog(TestData.AUDIO_FOR_SINGLE_INTENTS[0][0])

        with allure.step("Check that metrics are displayed in chat under system answer"):
            assert self.enova_chat.is_versions_in_chat(), "Metrics is not present in chat after"
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Check that metrics contained not empty data"):
            assert self.enova_chat.is_data_in_versions(), "Metrics are empty, no data is in metrics"

    """Wake up word state in Settings by default"""

    @pytest.mark.skip
    @allure.title("Wake up word settings by default")
    def test_wuw_settings_default(self, driver, login, server, user, protocol, language):
        self.settings = SettingsInApp(driver)
        self.customers_page = ChooseCustomerScreen(driver)
        self.enova_chat = EnovaChatPage(driver)

        with allure.step("Open settings and check that wake up word is enabled by default"):
            assert self.settings.is_wuw_switched_on(), "Wake up word is disabled by default"

        with allure.step("Open chat for Enova customer"):
            self.customers_page.open_chatmode_for_customer("Enova")
        with allure.step("Check that 'Hey Nova' text is presented on screen"):
            assert self.enova_chat.is_wuw_text(), "WuW text is not presented on the screen"
            assert self.enova_chat.get_wuw_text() == 'Say "Hey Nova" or press\nmic button and ask a question' or self.enova_chat.get_wuw_text() == 'Скажите "Hey Nova" или нажмите\nкнопку микрофона и задайте вопрос', \
                "WuW text is not presented on the screen"
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    """Ware up Word enabled test"""

    @pytest.mark.skip
    @allure.title("Wake up word enabled test")
    def test_wuw_enabled(self, driver, login, server, user, protocol, language):
        self.settings = SettingsInApp(driver)
        self.customers_page = ChooseCustomerScreen(driver)
        self.enova_chat = EnovaChatPage(driver)

        with allure.step("Switch on 'Wake up Word' option in Settings"):
            self.settings.wuw_switch_on()
        with allure.step("Open chat for Enova customer"):
            self.customers_page.open_chatmode_for_customer("Enova")
        with allure.step("Say 'Hey Nova' in chat"):
            self.enova_chat.say_in_enova_chat(TestData.AUDIO_FOR_SINGLE_INTENTS[1][0])

        with allure.step("Check that listening mode is on"):
            assert self.enova_chat.is_listening_mode_on(), "Listening mode is off, Mic button is displayed"
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    """Ware up Word disabled test"""

    @pytest.mark.skip
    @allure.title("Wake up word disabled test")
    def test_wuw_disabled(self, driver, login, server, user, protocol, language):
        self.settings = SettingsInApp(driver)
        self.customers_page = ChooseCustomerScreen(driver)
        self.enova_chat = EnovaChatPage(driver)

        with allure.step("Switch off 'Wake up Word' option in Settings"):
            self.settings.wuw_switch_off()
        with allure.step("Open chat for Enova customer"):
            self.customers_page.open_chatmode_for_customer("Enova")
        with allure.step("Say 'Hey Nova' in chat"):
            self.enova_chat.say_in_enova_chat(TestData.AUDIO_FOR_SINGLE_INTENTS[1][0])
            self.enova_chat.pause(6)
        with allure.step("Check that listening mode is off"):
            assert self.enova_chat.is_listening_mode_off(), "Listening mode is on, but WuW is disabled"
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    """Enova chat test with any modes"""

    @pytest.mark.skip
    @pytest.mark.parametrize("mode_title", [
        "Default stream_audio",
        "Default put_audio",
    ])
    @pytest.mark.parametrize("audio_path, audio_lang, expected_answer", [
        ("..\\TestData\\AudioData\\tell_me_about_you_en.mp3", "English", "Hello! I'm autotest skill"),
        ("..\\TestData\\AudioData\\tell_me_about_you_ru.mp3", "Russian", "Привет! Я автотест скилл"),
    ])
    @allure.title("Enova chat test")
    def test_enova_chat(self, driver, login, server, user, protocol, language, mode_title, audio_path, audio_lang, expected_answer):
        if language == audio_lang:
            self.settings = SettingsInApp(driver)
            self.customers_page = ChooseCustomerScreen(driver)
            self.enova_chat = EnovaChatPage(driver)

            with allure.step("Open chat for Enova customer"):
                self.customers_page.open_chatmode_for_customer("Enova")
            with allure.step(f"Switch to {mode_title} mode"):
                self.enova_chat.select_mode(mode_title)
                allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
                self.enova_chat.pause(1)
            with allure.step("Make request in chat"):
                self.enova_chat.send_question_in_chat_not_dialog(audio_path)
            with allure.step("Check that answer is displayed in chat"):
                assert self.enova_chat.is_answer_in_chat(), "Answer is not displayed in chat"
            with allure.step("Check that answer is correct"):
                assert self.enova_chat.get_answer_from_chat() == expected_answer, "Answer is not an expected answer"
                allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        else:
            with allure.step(f"Test is skipped, because customer language is {language}, but audio language is {audio_lang}"):
                pass

    """Test image content in Enova chat"""

    @pytest.mark.skip
    @pytest.mark.parametrize("mode_title", [
        "Default stream_audio",
        "Default put_audio",
    ])
    @pytest.mark.parametrize("audio_path, audio_lang", [
        ("..\\TestData\\AudioData\\image_content_en.mp3", "English"),
        ("..\\TestData\\AudioData\\image_content_ru.mp3", "Russian"),
        ("..\\TestData\\AudioData\\image_url_content_en.mp3", "English"),
        ("..\\TestData\\AudioData\\image_secure_url_content_en.mp3", "English"),
    ])
    @allure.title("Test image content in Enova chat")
    def test_image_content_enova_chat(self, driver, login, server, user, protocol, language, audio_path, audio_lang, mode_title):
        if language == audio_lang:
            self.enova_chat = EnovaChatPage(driver)
            self.enova_actions = EnovaActions(driver)

            with allure.step(f"Ask question from intent with image content and check that image in answer is displayed in chat. Mode is {mode_title}"):
                self.enova_actions.make_request_enova_chat(audio_path, mode_title)

            with allure.step("Check that image content is displayed in answer"):
                assert self.enova_chat.is_image_content(), "Image is not displayed in answer"
                allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        else:
            with allure.step(f"Test is skipped, because customer language is {language}, but audio language is {audio_lang}"):
                pass

    """Test text content in Enova chat"""

    @pytest.mark.skip
    @pytest.mark.parametrize("mode_title", [
        "Default stream_audio",
        "Default put_audio",
    ])
    @pytest.mark.parametrize("audio_path, expected_text", [
        ("..\\TestData\\AudioData\\text_content_en.mp3", "text for testing"),
    ])
    @allure.title("Test text content in Enova chat")
    def test_text_content_enova_chat(self, driver, login, server, user, protocol, language, audio_path, expected_text, mode_title):
        self.enova_chat = EnovaChatPage(driver)
        self.enova_actions = EnovaActions(driver)

        with allure.step(f"Ask question from intent with text content and check that text in answer is displayed in chat. Mode is {mode_title}"):
            self.enova_actions.make_request_enova_chat(audio_path, mode_title)

        with allure.step("Check that text content is displayed in answer"):
            assert self.enova_chat.is_text_content(), "Text is not displayed in answer"
            assert self.enova_chat.get_text_from_text_content() == expected_text
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    """Unregistering device test"""

    @pytest.mark.skip
    @allure.description("Unregistering device test")
    def test_logout(self, driver, login, server, user, protocol, language):
        self.login_page = LoginPage(driver)
        self.settings = SettingsInApp(driver)
        self.customers_page = ChooseCustomerScreen(driver)

        with allure.step("Open Settings -> Device page and click 'Unregister' button"):
            self.settings.unregister_device()

        with allure.step("Check that login page is opened"):
            assert self.login_page.is_login_page()
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

        with allure.step("Check that 'Email' field is empty and after click 'Submit' button "
                         "messsage about invalid email is displayed"):
            self.login_page.click_send_button()
            assert self.login_page.is_warning_red_text()
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


    """Meetings button is present in Enova chat"""

    @pytest.mark.skip
    @allure.description("Meetings button is present in Enova chat test")
    def test_meeting_button_present(self, driver, login, server, user, protocol, language):
        self.customers_page = ChooseCustomerScreen(driver)
        self.enova_chat = EnovaChatPage(driver)

        with allure.step("Open Enova chat"):
            self.customers_page.open_chatmode_for_customer("Enova")
        with allure.step("Check that meeting button is present in chat"):
            assert self.enova_chat.is_meeting_button()
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    """Create meetings: meeting creation window is opened"""

    @pytest.mark.skip
    @allure.description("Opening meeting creation page")
    def test_open_create_meeting_page(self, driver, login, server, user, protocol, language):
        self.meetings = MeetingPage(driver)
        with allure.step("Open 'Create meeting' page"):
            self.meetings.open_create_meeting_page()
        with allure.step("Check that 'Create meeting' page is opened"):
            assert self.meetings.is_create_meeting_page(), \
                "'Create meeting' page is not opened or page header is incorrect"
        with allure.step("Check 'Create meeting' header text"):
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            assert self.meetings.get_meeting_create_header_text() == "New Meeting" or self.meetings.get_meeting_create_header_text() == "Новое совещание", \
                "Incorrect header text on 'Create meeting' page"

    """Create meetings: meetings name is presented"""

    @pytest.mark.skip
    @allure.description("Check meeting name on 'Create meeting' page")
    def test_meeting_name_on_create_meeting_page(self, driver, login, server, user, protocol, language):
        self.meetings = MeetingPage(driver)
        with allure.step("Open 'Create meeting' page"):
            self.meetings.open_create_meeting_page()

        with allure.step("Check that meeting name is presented on Create meeting page"):
            assert self.meetings.is_meeting_name_on_create_meeting_page(), \
                "Meeting name field is not presented on 'Create meeting' page "
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

        with allure.step("Check meeting name on 'Create meeting' page"):
            # current_datetime = str(datetime.now()).split(" ")
            # time = current_datetime[1].split(".")[0]
            # data = current_datetime[0].split("-")
            assert re.match(TestData.MEETING_NAME_REG, self.meetings.get_meeting_name_create_meeting_page()), \
                "Format meeting name on Create meeting page is incorrect"

    """Create meetings: Topics are presented"""

    @pytest.mark.skip
    @allure.description("Check topics on 'Create meeting' page")
    def test_tags_on_create_meeting_page(self, driver, login, server, user, protocol, language):
        self.meetings = MeetingPage(driver)
        with allure.step("Open 'Create meeting' page"):
            self.meetings.open_create_meeting_page()

        with allure.step("Check that topics are presented on Create meeting page"):
            assert self.meetings.is_topics_on_create_meeting_page(), \
                "Topics area is not presented on 'Create meeting' page"
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            assert len(self.meetings.get_topics_list_create_meeting_page()) > 0, \
                "Topics are not present on 'Create meeting' page"

    """Create meetings: add topic"""

    @pytest.mark.skip
    @allure.description("Add new topic on 'Create meeting' page")
    def test_add_new_topic_on_create_meeting_page(self, driver, login, server, user, protocol, language):
        self.meetings = MeetingPage(driver)
        new_topic_name = "New topic"
        with allure.step("Open 'Create meeting' page"):
            self.meetings.open_create_meeting_page()
            topics_list = self.meetings.get_topics_list_create_meeting_page()
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Click 'Add topic' button"):
            self.meetings.click_add_topic_button()
        with allure.step(f"Set new topic name: {new_topic_name}"):
            self.meetings.set_new_topic_name(new_topic_name)
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Click 'OK' button"):
            self.meetings.click_ok_on_new_topic_form()
        with allure.step(f"Check that new topic '{new_topic_name}' is added"):
            new_topic_list = self.meetings.get_topics_list_create_meeting_page()
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            assert len(new_topic_list) == len(topics_list) + 1, \
                "Meetings list is incorrect after adding new topic"
        with allure.step("Check that added topic is 'New topic'"):
            assert self.meetings.get_topic_name(new_topic_list[-1]) == new_topic_name, \
                "Name of added topic is incorrect"

    """Create new meeting"""

    @pytest.mark.skip
    @allure.description("Create new meeting test")
    def test_create_new_meeting(self, driver, login, server, user, protocol, language):
        self.meetings = MeetingPage(driver)
        with allure.step("Create new meeting with default name and without topics"):
            self.meetings.create_new_meeting()

        with allure.step("Check that meeting is created and contains name, text area and mic button"):
            assert self.meetings.is_meeting_created(), \
                "Meeting is not created or created incorrectly"
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
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
    def test_new_meeting_name(self, driver, login, server, user, protocol, language, meeting_name):
        self.meetings = MeetingPage(driver)
        with allure.step(f"Create new meeting with name: {meeting_name}"):
            self.meetings.create_new_meeting(meeting_name)
        with allure.step("Check that meeting is created and contains name, text area and mic button"):
            assert self.meetings.is_meeting_created(), \
                "Meeting is not created or created incorrectly"
        with allure.step("Check name of created meeting"):
            assert self.meetings.get_meeting_name() == meeting_name, \
                f"Name of created meeting is not {meeting_name}"
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    """Meeting screen: edit meeting button"""

    @pytest.mark.skip
    @allure.description("Check that Edit button is present for meeting and Edit window can be opened")
    def test_edit_meeting_button(self, driver, login, server, user, protocol, language):
        self.meetings = MeetingPage(driver)
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
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    """Meeting screen: meeting markers button"""

    @pytest.mark.skip
    @allure.description("Check that Markers button is present for meeting and markers form can be opened")
    def test_markers_meeting_button(self, driver, login, server, user, protocol, language):
        self.meetings = MeetingPage(driver)
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
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    """Meeting screen: meeting details button"""

    @pytest.mark.skip
    @allure.description("Check that Details button is present for meeting and is disabled for empty meeting")
    def test_markers_meeting_button(self, driver, login, server, user, protocol, language):
        self.meetings = MeetingPage(driver)
        with allure.step("Create new meeting"):
            self.meetings.create_new_meeting()

        with allure.step("Check that 'Details' button is present on Meeting page"):
            assert self.meetings.is_meeting_details_button(), \
                "'Details' button is not found on Meeting page"

        with allure.step("Check that 'Details' button is disabled for empty meeting"):
            assert not self.meetings.is_enabled_meeting_details_button(), \
                "'Details' button is enabled for empty meeting"
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    """Change meeting name"""

    @pytest.mark.skip
    @allure.description("Changing meeting name test")
    @pytest.mark.parametrize("new_name", [
        "New meeting",
        "Новый митинг",
        "!@#$%$%^^",
    ])
    def test_change_meeting_name(self, driver, login, server, user, protocol, language, new_name):
        self.meetings = MeetingPage(driver)
        with allure.step("Create new meeting"):
            self.meetings.create_new_meeting()
        with allure.step("Open 'Edit meeting' page"):
            self.meetings.open_meeting_edit_page()
        with allure.step("Change meeting name"):
            self.meetings.set_meeting_name(new_name)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step("Save changes in meeting"):
            self.meetings.save_changes_in_meeting()

        with allure.step("Check new meeting name"):
            assert self.meetings.get_meeting_name() == new_name, \
                f"Name of created meeting is not {new_name}"
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    """Change meeting topics"""

    @pytest.mark.skip
    @allure.description("Changing meeting topics test")
    def test_change_meeting_topics(self, driver, login, server, user, protocol, language):
        self.meetings = MeetingPage(driver)
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
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    """Meeting recording audio"""

    @pytest.mark.skip
    @allure.description("Meeting recording audio test")
    @pytest.mark.parametrize("audio_path, audio_lang, expected_text_path", [
        ("..\\TestData\\AudioData\\what_time_is_it.mp3", "English", "..\\TestData\\AudioData\\what_time_is_it.txt"),
        ("..\\TestData\\AudioData\\add_hoc_testing.mp3", "English", "..\\TestData\\AudioData\\add_hoc_testing.txt"),
        ("..\\TestData\\AudioData\\test_in_google.mp3", "Russian", "..\\TestData\\AudioData\\test_in_google.txt"),
    ])
    def test_record_meeting(self, driver, login, server, user, protocol, language, audio_path, audio_lang, expected_text_path):
        if language == audio_lang:
            self.meetings = MeetingPage(driver)
            with allure.step("Create new meeting"):
                self.meetings.create_new_meeting()
            with allure.step(f"Start meeting recording, play audio: {audio_path} and stop meeting"):
                recording_time = self.meetings.record_meeting(audio_path)

            with allure.step("Check that meeting text is presented"):
                assert self.meetings.is_meeting_text(), "Meeting text is not presented"
            meeting_text = self.meetings.get_meeting_text()
            with allure.step(f"Meeting text: {' '.join(meeting_text)}"):
                pass

            with allure.step("Check that Mic button is disabled and Details button is enabled"):
                assert self.meetings.is_enabled_meeting_details_button(), "Details button is disabled"
                assert not self.meetings.is_enabled_meeting_recording_button(), "Mic button is enabled"
                allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

            with allure.step("Check Details menu"):
                self.meetings.open_meeting_detais()
            with allure.step("Check details list"):
                assert self.meetings.get_details_list() == TestData.MEETING_DETAILS_LIST, \
                    "meeting details menu is incorrect"
                allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

            with allure.step("Check subtitles"):
                self.meetings.open_meeting_subtitles()
                assert self.meetings.is_meeting_subtitles_page(), \
                    "Meeting subtitles page are not opened or has incorrect header"
                allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

            meeting_subtitles = self.meetings.get_meeting_subtitles()
            with allure.step(f"Meeting subtitles: {meeting_subtitles}"):
                pass

            with allure.step("Compare subtitles and text of meeting"):
                assert " ".join(meeting_text) == self.meetings.pars_subtitles(meeting_subtitles), \
                    "Meeting text and subtitles are not the same"
            self.meetings.back_to_meeting_from_details()

            with allure.step("Check meeting time"):
                time_in_app = self.meetings.get_meeting_recording_time()
                time_in_app = time_in_app.split(":")
                t = int(time_in_app[0]) * 60 * 60 + int(time_in_app[1]) * 60 + int(time_in_app[2])
                assert (t <= recording_time <= t+4), "Meeting time is incorrect"
                allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

            with open(expected_text_path) as f:
                expected_text = f.read()
            wer = self.meetings.wer(' '.join(meeting_text), expected_text)
            with allure.step(f"Meeting WER: {wer}"):
                pass

        else:
            with allure.step(f"Test is skipped, because customer language is {language}, but audio language is {audio_lang}"):
                pass
