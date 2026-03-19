from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.get('https://amazon.in')
wait = WebDriverWait(driver, 10)
driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys('Watch')
driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()
print(driver.find_element(By.XPATH, "(//div[@class='a-row a-size-base a-color-base'])[5]/../../..//div[2]//div//div").text)
