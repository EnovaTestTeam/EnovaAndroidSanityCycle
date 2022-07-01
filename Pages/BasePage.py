from playsound import playsound
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_back_android(self):
        self.driver.back()

    def click_by_locator(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def click_by_element(self, element):
        element.click()

    def send_keys_by_locator(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def send_keys_by_element(self, element, text):
        element.send_keys(text)

    def clear_element_by_locator(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).clear()

    def clear_element_by_element(self, element):
        element.clear()

    def get_element_text_by_locator(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    def get_element_text_by_element(self, element):
        return element.text

    def is_element_by_locator(self, locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
        return bool(element)

    def find_elements(self, locator):
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        return elements

    def find_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    def is_element_checked_by_locator(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        if element.get_attribute("checked") == "true":
            return True
        else:
            return False

    def is_element_checked_by_element(self, element):
        if element.get_attribute("checked") == "true":
            return True
        else:
            return False

    def swipe_left_by_element(self, element):
        x = element.location['x'] + element.size['width'] / 2
        y = element.location['y'] + element.size['height'] / 2
        self.driver.swipe(x, y, 35, y, 200)

    def swipe_right_by_element(self, element):
        x = element.location['x'] + element.size['width'] / 2
        y = element.location['y'] + element.size['height'] / 2
        self.driver.swipe(0, y, x, y, 200)

    def swipe_top(self):
        x = self.driver.get_window_size()["width"] / 2
        y = self.driver.get_window_size()["height"] - 50
        print(y)
        self.driver.swipe(x, y, x, 50, 400)

    def pause(self, seconds):
        time.sleep(seconds)

    def play(self, audio_path):
        print(audio_path)
        playsound(audio_path)
