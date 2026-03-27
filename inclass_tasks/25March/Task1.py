import os
import time
from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Setup Chrome options (keeps browser open after script ends)
options = ChromeOptions()
options.add_experimental_option('detach', True)

# Initialize driver
driver = Chrome(options=options)
driver.implicitly_wait(10)  # implicit wait for element loading

# Open Pinterest
driver.get("https://in.pinterest.com/")

# Create folder to store screenshots
folder = os.path.join(os.getcwd(), 'practice')
os.makedirs(folder, exist_ok=True)

# Generate timestamp for unique filenames
time_stamp = time.strftime("%Y%m%d%H%M%S")

# Take full page screenshot
driver.save_screenshot(f'{folder}/entirePage_{time_stamp}.png')

sleep(2)

# Locate the target image element (fragile XPath, but keeping your logic)
ele = driver.find_element(
    By.XPATH,
    '//*[@id="mweb-unauth-container"]/div/div/div/div[4]/div[2]/div/div/div/div[2]/div/div/img'
)

# Hover over the element (not strictly needed, but kept)
action = ActionChains(driver)
action.move_to_element(ele).pause(2).perform()

# Take screenshot of the specific element
ele.screenshot(f'{folder}/Pinterest_{time_stamp}.png')

sleep(5)

# Close browser
driver.quit()
