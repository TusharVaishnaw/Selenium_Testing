'''
forward traversing / or //          parent to child
backward traversiing /..            child to parent

steps for
1 identify the static
2 move to the common parent
3 fetch the dynamic element
//td[text()='Cierra']/..//td[5]
'''
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach", True)
# o.add_argument('--headless')
# o.add_argument('--incognito')


driver = Chrome(options=o)
# driver.get('https://demoqa.com/webtables')
# print(driver.find_element(By.XPATH, "//td[text()='Vega']/..//td[6]").text)

# driver.get('https://the-internet.herokuapp.com/tables')
# print(driver.find_element(By.XPATH,"//td[text()='Frank']/..//td[4]").text)
#
# '''using silbing'''
#
# # following sibling
# driver.get('https://the-internet.herokuapp.com/tables')
# print(driver.find_element(By.XPATH,"//td[text()='Frank']//following-sibling::td[2]").text)
# # preceding sibling
#
# driver.get('https://the-internet.herokuapp.com/tables')
# print(driver.find_element(By.XPATH,"//td[text()='Frank']//preceding-sibling::td[1]").text)

sleep(7)
driver.quit()
