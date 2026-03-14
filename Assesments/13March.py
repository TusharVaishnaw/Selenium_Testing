from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

# Task 1 : Using ID
driver.get("https://www.amazon.in")
driver.maximize_window()
sleep(2)
driver.find_element(By.ID, "nav-global-location-popover-link").click()
sleep(2)

# Task 2 : Using Name
driver.get("https://www.facebook.com")
sleep(2)
driver.find_element(By.NAME, "email").send_keys("your_email")
driver.find_element(By.NAME, "pass").send_keys("your_password")
sleep(2)

# Task 3 : Using ID and PARTIAL LINK TEXT
driver.get("https://www.amazon.in")
sleep(2)
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Mobiles")
driver.find_element(By.ID, "nav-search-submit-button").click()
sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT, "Samsung").click()
sleep(2)

# Task 4 : Using LINK TEXT and PARTIAL LINK TEXT
driver.get("https://www.selenium.dev/")
sleep(2)
driver.find_element(By.LINK_TEXT, "Downloads").click()
sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "Other Languages").click()
sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "Register").click()
sleep(2)
print(driver.title)

# driver.quit()
