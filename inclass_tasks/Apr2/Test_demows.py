import os
from time import sleep
import time

import pytest
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option('detach', True)
o.add_experimental_option("prefs", {"safebrowsing.enabled": True})
o.add_argument("--disable-notifications")


@pytest.fixture(scope='class')
def setup():
    driver = Chrome(options=o)
    driver.implicitly_wait(10)
    driver.get("https://demowebshop.tricentis.com/register")
    a = 1
    yield driver
    sleep(3)
    driver.close()


class TestRegister:

    def test_gender(self, setup):
        driver=setup
        driver.find_element(By.ID, "gender-male").click()
        setup.find_element(By.ID, "gender-female").click()

    # @pytest.mark.regression
    def test_firstname(self):
        driver.find_element(By.ID, "FirstName").send_keys("Tushar")
    #
    # def test_secondname(self):
    #     driver.find_element(By.ID, "LastName").send_keys("Vaishnaw")
    #
    # def test_email(self):
    #     driver.find_element(By.ID, "Email").send_keys("tvw11@gmail.com")
    #
    # def test_password(self):
    #     driver.find_element(By.ID, "Password").send_keys("password")
    #
    # def test_cnfmpsw(self):
    #     driver.find_element(By.ID, "ConfirmPassword").send_keys("password")
    #
    # def test_register_click(self):
    #     driver.find_element(By.ID, "register-button").click()
