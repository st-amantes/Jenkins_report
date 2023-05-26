import pytest
from selene import browser
from selene.support import webdriver


@pytest.fixture(scope="function", autouse=True)
def driver_setting():
    chrome_options = webdriver.CromeOptions()
    browser.config.driver_options = chrome_options
    browser.config.base_url = "https://demoqa.com"
    browser.driver.set_window_size(1980, 1080)


    yield

    browser.quit()