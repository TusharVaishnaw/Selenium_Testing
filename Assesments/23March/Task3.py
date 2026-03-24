from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By

# Setup Chrome (detach helps debugging)
options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = Chrome(options=options)

driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.implicitly_wait(10)

# Close login popup
driver.find_element(By.XPATH, '//span[text()="✕"]').click()

actions = ActionChains(driver)

# Scroll to Myntra link and open in new tab
myntra = driver.find_element(By.XPATH, '//a[@href="https://www.myntra.com/"]')
actions.scroll_from_origin(ScrollOrigin.from_element(myntra), 0, 100).pause(1).perform()
myntra.click()

# Switch to Myntra tab and print details
driver.switch_to.window(driver.window_handles[1])
print(driver.current_window_handle, driver.title, driver.current_url)

# Open Shopsy and print details
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH, '//a[@href="https://www.shopsy.in"]').click()
driver.switch_to.window(driver.window_handles[3])
print(driver.current_window_handle, driver.title, driver.current_url)

sleep(5)
driver.quit()
