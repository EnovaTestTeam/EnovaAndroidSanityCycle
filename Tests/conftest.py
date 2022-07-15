import pytest
from appium import webdriver
from Pages.LoginPage import LoginPage
from TestData.config import TestData


@pytest.fixture(scope='function')
def driver():
    test_data = TestData()

    driver = webdriver.Remote("http://localhost:4723/wd/hub", test_data.DESIRED_CAPABILITIES)

    yield driver
    driver.close_app()
    driver.quit()


@pytest.fixture
def login(driver, server, user, protocol, language):
    login_page = LoginPage(driver)

    login_page.login(server, user, protocol, language)
    #yield driver


