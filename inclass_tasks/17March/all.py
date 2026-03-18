from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

o = ChromeOptions()
o.add_experimental_option("detach", True)
'''
implicit wait - global wait, wait till element found or time expired whichever first
'''
driver = Chrome(options=o)

driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
# sleep(3)
driver.find_element(By.XPATH, '//button').click()
# sleep(5)
wait = WebDriverWait(driver,10)
# print(wait.until(EC.visibility_of_element_located((By.XPATH, '(//h4)[2]'))).text)
print(wait.until(EC.visibility_of_element_located((By.XPATH, " //div[@id='finish']"))).text)
# print(element.text)
# print(driver.find_element(By.ID, 'finish').text)
# sleep(20)
driver.quit()
