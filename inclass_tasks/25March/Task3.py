from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

options = ChromeOptions()
options.add_experimental_option("detach", True)

driver = Chrome(options=options)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]').send_keys("mobiles")
sleep(2)
driver.find_element(By.XPATH, '//div[@aria-rowindex="4"]').click()

sleep(2)
driver.find_element(By.XPATH, '//span[@class="a-dropdown-label"]').click()
driver.find_element(By.XPATH, '//a[.="Newest Arrivals"]').click()
driver.find_element(By.XPATH, '//span[.="Free Shipping"]').click()

name = driver.find_element(By.XPATH, '(//div[@data-cy="title-recipe"])[1]').text
price = driver.find_element(By.XPATH, '(//span[@class="a-price-whole"])[1]').text

print(f"{name} = {price}")

sleep(5)
driver.quit()
