from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

o = ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)
driver.implicitly_wait(10)

'''find_elements returns a list'''
# driver.get('https://www.google.com')
# for i in driver.find_elements(By.TAG_NAME, 'a'):
#     print(i.text)

'''GET ATTRIBUTE METHOD'''
# print(driver.find_element(By.XPATH,"//a[@class='gb_A']").get_attribute('aria-label'))


'''
for c
c.is_displayed()
c.is_enabled()
c.is_selected()
'''
# driver.get("https://the-internet.herokuapp.com/checkboxes")
# c1 = driver.find_element(By.XPATH, "//input[1]")
# c2 = driver.find_element(By.XPATH, "//input[2]")
# print(c1.is_displayed())
# print(c1.is_enabled())
# print(c1.is_selected())
# print(c2.is_selected())

driver.get('https://amazon.in')
wait = WebDriverWait(driver, 10)
l = driver.find_elements(By.XPATH, "(//div[@id='nav-main'])//a")
for i in l:
    if i.text != '':
        print(i.text, "= ", i.get_attribute('href'))



# driver.quit()
