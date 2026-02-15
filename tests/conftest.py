
import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser.config.driver = driver

    yield driver
