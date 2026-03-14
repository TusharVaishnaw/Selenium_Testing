from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

'''
driver.get("https://amazon.com")
driver.maximize_window()

sleep(2)
username =driver.find_element(By.ID,'twotabsearchtextbox')
username.send_keys('shirts')
sleep(1)
srh=driver.find_element(By.ID,'nav-search-submit-button')
srh.click()
sleep(10)
driver.quit()
'''

'''
driver.get("https://demoqa.com/text-box")
sleep(2)
# driver.find_element(By.CLASS_NAME, 'nav-input.nav-progressive-attribute').send_keys('shit')
driver.find_element(By.TAG_NAME, 'input').send_keys('tushar')
# sleep(1)
driver.find_element(By.TAG_NAME, 'input').send_keys('tushar@gmail.com')
# driver.find_element(By.TAG_NAME, 'textarea').send_keys('tushar vaishnaw')

# driver.find_element(By.ID, 'nav-search-submit-button').click()
'''


# driver.get("https://www.amazon.in")
#
# sleep(3)
# # driver.find_element(By.LINK_TEXT, 'Mobiles').click()
# driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search Amazon.in"]').click()
# sleep(10)
# driver.quit()

driver.get("https://selenium.dev")
sleep(3)
driver.find_element(By.LINK_TEXT,'Downloads').click()
sleep(3)
driver.find_element(By.LINK_TEXT,'other languages exist').click()

sleep(3)
print(driver.title)
driver.quit()

