'''
open amazon
search mobiles
click on search icon
'''

from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get('https://flipkart.com')
sleep(3)
driver.find_element(By.XPATH,"//span[@class='b3wTlE']").click()
sleep(2)
driver.find_element(By.XPATH, "//input[@class='nw1UBF v1zwn25']").send_keys('SONY PlayStation5 Console')
driver.find_element(By.XPATH,"//button[@class='XFwMiH']").click()
sleep(3)
driver.find_element(By.XPATH,"(//div[@class='WNv7PR'])[2]").click()

print(driver.find_element(By.XPATH, "((//div[@class='RGLWAk'])[1]/..//div)[11]").text)
# sleep(7)
# driver.quit()
