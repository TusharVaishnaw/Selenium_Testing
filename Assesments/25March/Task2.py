import time
from time import sleep
import os

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

options = ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--disable-notifications')

driver = Chrome(options=options)
driver.implicitly_wait(10)

driver.get('https://www.lenskart.com/')
driver.maximize_window()
driver.find_element(By.XPATH, "//a[@id='lrd1']").click()

expected = 'https://www.lenskart.com/eyeglasses.html'
actual = driver.current_url
assert expected == actual, "URL Mismatch"

driver.find_element(By.XPATH, "//select[@id='sortByDropdown']").click()
driver.find_element(By.XPATH, "//option[.='Most Viewed']").click()

# ss
folder = os.path.join(os.getcwd(), 'Lenskart_practice')
os.makedirs(folder, exist_ok=True)
time_stamp = time.strftime("%Y%m%d%H%M%S")
driver.save_screenshot(f'{folder}/lenskart_{time_stamp}.png')

sleep(5)
driver.close()
