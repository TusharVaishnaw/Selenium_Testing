# Task4:
# 1 open internetheroku alert
# 2 click all the alerts
# 3  print their message and accept them

from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option('detach', True)
o.add_experimental_option("prefs", {"safebrowsing.enabled":True})
o.add_argument("--disable-notifications")
driver = Chrome(options=o)
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

a1=driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']")
a1.click()
sleep(1)
a1=driver.switch_to.alert
print(a1.text)
a1.accept()


a2=driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']")
a2.click()
sleep(1)
a2=driver.switch_to.alert
print(a2.text)
a2.accept()


a3=driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']")
a3.click()
sleep(1)
a3=driver.switch_to.alert
print(a3.text)
a3.send_keys('Tushar Vaishnaw is supreme')
sleep(1)
a3.accept()
