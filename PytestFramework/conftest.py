import pytest
from selenium import webdriver
from config.env import ConfigReader


@pytest.fixture
def setup_and_teardown():
    #Reading the config
    config = ConfigReader.read_config()
    env = config["qa"]
    base_url = env["base_url"]
    #Setting up (before the main testing)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_url)
    yield driver    #test runs here
    #Teardown - done after the test
    driver.quit()