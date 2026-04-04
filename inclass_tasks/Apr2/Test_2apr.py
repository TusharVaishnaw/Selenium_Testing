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


# @pytest.mark.skip(reason="Feature not ready")
# def test_login():
#     assert True
#
#
# flag = 'bombed'
#
#
# @pytest.mark.skipif(flag == 'bombed', reason="Servers bombed- dont execute")
# def test_logout():
#     assert True


# @pytest.mark.parametrize('name,password',[('standard_user','secret_sauce'),('asda','adsas'),('standard_user','secret_sauce')])
# def test_sd(name,password):
#     driver.find_element(By.ID,"user-name").send_keys(name)
#     driver.find_element(By.ID,"password").send_keys(password)
#     driver.find_element(By.ID,"login-button").click()
#     assert driver.current_url == 'https://www.saucedemo.com/inventory.html', driver.refresh()
#     driver.back()


# @pytest.fixture(autouse=True)
# def greet():
#     print('\nlesgoooo greet func print 1')
#     yield
#     print('\ngreet died!! :(')
#
#
# def test_func1():
#     print('func1 born')
#     print('func1 died')
#
#
# def test_func2():
#     print('func2 born')
#     print('func2 died')

@pytest.fixture(scope='class')
def setup():
    driver = Chrome(options=o)
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")
