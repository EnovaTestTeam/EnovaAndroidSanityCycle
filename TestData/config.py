

class TestData:
    APPLICATION = r"C:\Users\ruvkuminov\eNova_Beta_1.1.4.179.apk"
    DEVICE = "emulator-5554"  # "VFFDU19B08002278"

    DESIRED_CAPABILITIES = {'app': APPLICATION,
                            'appPackage': 'com.harman.enova.beta',
                            'appActivity': 'com.harman.enova.MainActivity',
                            'platformName': 'Android', 'deviceName': DEVICE,
                            'autoGrantPermissions': True,
                            'adbExecTimeout': 500000,
                            'newCommandTimeout': 500000
                            }

    LOGIN_DATA = {"SERVER": "US West", "USER_NAME": "tbd@gmail.com", "PROTOCOL": "WebSocket", "LANGUAGE": "English"}
    SETTINGS_DATA = {"pauseDetectionTimeoutLayout": "5000"}
    CUSTOMER = "Enova"

    AUDIO_FOR_SINGLE_INTENTS = [
        ("..\\TestData\\AudioData\\what_time_is_it.mp3", "What time is it", ""),
        ("..\\TestData\\AudioData\\hey_nova.mp3", "Hey nova", ""),
    ]

    AUDIO_FOR_DIALOGS = []

    MEETING_NAME_REG = r"[a-z|A-Z]*_[0-9]{2}_[a-z|A-Z]*_[0-9]{2}_[0-9]{2}:[0-9]{2}:[0-9]{2}"

    MEETING_DETAILS_LIST = ["Important Notes", "Subtitles", "Meeting Analytics Report", "Meeting Minutes", "Refresh meeting details"]



