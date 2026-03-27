import os
import time
from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

options = ChromeOptions()
options.add_experimental_option('detach', True)

driver = Chrome(options=options)
driver.implicitly_wait(10)

driver.get("https://in.pinterest.com/")

folder = os.path.join(os.getcwd(), 'practice')
os.makedirs(folder, exist_ok=True)

time_stamp = time.strftime("%Y%m%d%H%M%S")

#ss1
driver.save_screenshot(f'{folder}/entirePage_{time_stamp}.png')

sleep(2)

ele = driver.find_element(
    By.XPATH,
    '//*[@id="mweb-unauth-container"]/div/div/div/div[4]/div[2]/div/div/div/div[2]/div/div/img'
)

action = ActionChains(driver)
action.move_to_element(ele).pause(2).perform()

#ss2
ele.screenshot(f'{folder}/Pinterest_{time_stamp}.png')

sleep(5)
driver.quit()
