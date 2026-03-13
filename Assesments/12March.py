from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

options = ChromeOptions()
options.add_experimental_option("detach", True)

driver = Chrome(options=options)

# Task 1
driver.get("https://www.wikipedia.org")
print(driver.title)

# Task 2
print(driver.current_url)

# Task 3
driver.refresh()
print(driver.title)
driver.get("https://www.amazon.com")
print(driver.title)
driver.back()
driver.close()
