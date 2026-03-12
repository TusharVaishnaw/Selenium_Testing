#open wikipedia
#from time import sleep
from selenium.webdriver import Chrome, ChromeOptions

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
#refresh
driver.get('https://wikipedia.org')
driver.refresh()
#fetch title
print(driver.title)
#open amazon
driver.get('https://amazon.com')
print(driver.title)
driver.back()
driver.close()
