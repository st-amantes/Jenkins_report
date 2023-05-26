import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def driver_setting():
    browser.config.base_url = "https://demoqa.com"
    browser.driver.set_window_size(1980, 1080)


    yield

    browser.quit()