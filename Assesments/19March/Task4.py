from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.get('https://demowebshop.tricentis.com/register')

driver.find_element(By.XPATH,"//input[@id='gender-male']").click()
driver.find_element(By.XPATH,"//input[@id='FirstName']").send_keys('Akshay')
driver.find_element(By.XPATH,"//input[@id='LastName']").send_keys('Khatri')
driver.find_element(By.XPATH,"//input[@id='Email']").send_keys('aksh11@gmail.com')
driver.find_element(By.XPATH,"//input[@id='Password']").send_keys('********')
driver.find_element(By.XPATH,"//input[@id='ConfirmPassword']").send_keys('********')

driver.find_element(By.XPATH,"//input[@id='register-button']").click()
