from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Setup Chrome with detach option (keeps browser open after script)
options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = Chrome(options=options)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

actions = ActionChains(driver)

# Scroll and hover over dropdown button
h1 = driver.find_element(By.XPATH, '//button[@class="dropbtn"]')
actions.scroll_by_amount(0, 1000).pause(2).move_to_element(h1).perform()

# Double click "Copy Text" button
dc = driver.find_element(By.XPATH, '//button[text()="Copy Text"]')
actions.pause(1).double_click(dc).perform()

# Drag and drop operation
dd1 = driver.find_element(By.ID, "draggable")
dd2 = driver.find_element(By.ID, "droppable")
actions.pause(2).drag_and_drop(dd1, dd2).perform()

sleep(2)
driver.quit()
