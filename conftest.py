import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=True)
def driver_setting():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(

        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    # browser.config.driver = driver
    # browser.config.base_url = "https://demoqa.com"
    # browser.driver.set_window_size(1980, 1080)
    # yield
    #
    # browser.quit()