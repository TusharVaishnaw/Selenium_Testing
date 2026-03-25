# Task3:
# 1 open 3 websites in 3 diff tabs
# 2 get title and id
# 3 close all tabs except the first one

from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
o = ChromeOptions()
o.add_experimental_option('detach', True)
o.add_experimental_option("prefs", {"safebrowsing.enabled":True})
o.add_argument("--disable-notifications")
driver = Chrome(options=o)
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")
print(driver.title,driver.current_window_handle)
driver.switch_to.new_window()
driver.get("https://demoqa.com/upload-download")
print(driver.title,driver.current_window_handle)
driver.switch_to.new_window()
driver.get("https://www.python.org/downloads/")
print(driver.title,driver.current_window_handle)
sleep(2)
driver.close()
sleep(1)
driver.switch_to.window(driver.window_handles[1])
driver.close()


sleep(5)
driver.quit()
