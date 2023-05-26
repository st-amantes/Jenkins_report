import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config

from utilits import attach

DEFAULT_BROWSER_VERSION = "100.0"

def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )

@pytest.fixture(scope="function")
def driver_setting(request):
    selenoid_browser =request.config.getoption("--browser")
    options = Options()
    selenoid_capabilities = {
        "browserName": selenoid_browser,
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

    browser = Browser(Config(driver=driver))
    yield

    attach.add_html(browser)
    attach.add_html(browser)
    attach.add_screenshot(browser)
