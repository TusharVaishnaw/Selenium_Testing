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
driver.get('https://amazon.in')
sleep(3)
driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys('Mobiles')
driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()
print(driver.find_element(By.XPATH,
                          "//span[contains(text(),'Samsung Galaxy M07')]/../../../..//span[@class='a-price']").text)

sleep(7)
driver.quit()
