from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Setup Chrome (detach keeps browser open for debugging)
options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = Chrome(options=options)

driver.get("https://www.nike.in/")
driver.maximize_window()
driver.implicitly_wait(10)

actions = ActionChains(driver)

# Hover and click on "Kids" section
kids = driver.find_element(By.XPATH, '//span[text()="Kids"]/..')
actions.move_to_element(kids).pause(1).click(kids).perform()

# Switch to new tab and open specific category
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH, '//a[@href="/elevate-their-style/c/94039"]').click()

# Select product and switch to product tab
driver.find_element(By.XPATH, '//div[text()="Nike Air Max Nova"]').click()
driver.switch_to.window(driver.window_handles[2])

# Choose size and add to bag
driver.find_element(By.XPATH, '//label[text()="UK 6 (EU 40)"]').click()
driver.find_element(By.XPATH, '//button[text()="Add to Bag"]').click()

sleep(5)
driver.quit()
