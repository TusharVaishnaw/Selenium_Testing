from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

o = ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)
# driver.implicitly_wait(10)
# driver.get("file:///T:/Downloadz/E22_Dropdowns.html")
# dropdown=driver.find_element(By.ID,'state')
# option=Select(dropdown)
# # option.select_by_visible_text("Maharastra")
# # option.select_by_index('4')
# option.select_by_value('MH')

# dropdown=driver.find_element(By.ID,'hobby')
# option=Select(dropdown)
# # option.select_by_visible_text("Maharastra")
# option.select_by_index(3)
# option.select_by_index(2)
#
# # option.select_by_value('MH')
#
# option.deselect_by_index(3)
#
# option.deselect_all()

driver.get("https://amazon.in")
sleep(3)
driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys('shoes for men')
sleep(3)

l=driver.find_elements(By.CSS_SELECTOR,"div.s-suggestion")
sleep(3)

for i in l:
    print(i.text)
sleep(3)

l[3].click()
# s = driver.find_elements(By.XPATH, "(//div[@class='s-suggestion-container'])")
sleep(3)
driver.quit()

