from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.get('https://flipkart.com')
wait = WebDriverWait(driver,10)

# driver.find_element(By.XPATH,"//span[@class='b3wTlE']").click()
# driver.find_element(By.XPATH, "//input[@class='nw1UBF v1zwn25']").send_keys('SONY PlayStation5 Console')
# driver.find_element(By.XPATH,"//button[@class='XFwMiH']").click()
wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='b3wTlE']"))).click()
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@class='nw1UBF v1zwn25']"))).send_keys('SONY PlayStation5 Console')
wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='XFwMiH']"))).click()
print(wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='RGLWAk'])[6]//a[2]"))).text)

# driver.find_element(By.XPATH,"(//div[@class='WNv7PR'])[2]").click()

# print(driver.find_element(By.XPATH, "(//div[@class='RGLWAk'])[6]//a[2]").text)
# sleep(7)
# driver.quit

# click add
# after creation get name = sal
