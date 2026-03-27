import os
from time import sleep
import time
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option('detach', True)
o.add_experimental_option("prefs", {"safebrowsing.enabled": True})
o.add_argument("--disable-notifications")
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.get("https://demowebshop.tricentis.com/register")


def test_gender():
    driver.find_element(By.ID, "gender-male").click()
    driver.find_element(By.ID, "gender-female").click()


def test_firstname():
    driver.find_element(By.ID, "FirstName").send_keys("Tushar")


def test_secondname():
    driver.find_element(By.ID, "LastName").send_keys("Vaishnaw")


def test_email():
    driver.find_element(By.ID, "Email").send_keys("tvw11@gmail.com")


def test_password():
    driver.find_element(By.ID, "Password").send_keys("password")


def test_cnfmpsw():
    driver.find_element(By.ID, "ConfirmPassword").send_keys("password")


def test_register_click():
    driver.find_element(By.ID, "register-button").click()
