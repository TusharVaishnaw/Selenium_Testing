from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
o = ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
actions = ActionChains(driver)

driver.get("https://x.com")
sleep(2)
su= driver.find_element(By.XPATH, "//iframe[contains(@src, 'accounts.google.com')]")
# su.click()
driver.switch_to.frame(su)
driver.find_element(By.XPATH,"//span[text()='Sign up with Google']").click()

driver.switch_to.window(driver.window_handles[1])

sleep(2)
driver.find_element(By.XPATH,"//span[text()='Create account']").click()


