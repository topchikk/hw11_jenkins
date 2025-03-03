import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.window_height = 720
    browser.config.window_width = 1280
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.quit()
