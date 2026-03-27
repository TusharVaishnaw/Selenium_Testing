import os
from time import sleep
import time
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option('detach', True)
o.add_experimental_option("prefs", {"safebrowsing.enabled":True})
o.add_argument("--disable-notifications")
driver = Chrome(options=o)
driver.implicitly_wait(10)

# driver.get("https://google.com")
# # print(driver.title)
#
# expected='GOOGLE'
# actual=driver.title
# assert expected==actual, "title mismatchh"

# driver.get("https://amazon.in")
# driver.find_element(By.LINK_TEXT,"Bestsellers").click()
# actual=driver.title
# expected='Amazon.in Bestsellers: The most popular items on Amazon'
# assert expected==actual, "title mismatchh"
# driver.save_screenshot(f'{folder}/ss1.png')

# driver.get("https://google.com")
# folder=os.path.join(os.getcwd(),'ssz')
# os.makedirs(folder,exist_ok=True)
#
#
# ele=driver.find_element(By.XPATH,"//textarea[@title='Search']")
# ele.screenshot(f'{folder}/ss_ele{time.strftime("%Y%m%d-%H%M%S")}.png')





sleep(5)
driver.quit()
