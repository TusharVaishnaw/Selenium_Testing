from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.get('https://amazon.in')
wait = WebDriverWait(driver, 10)
l = driver.find_elements(By.XPATH, "(//div[@id='nav-main'])//a")
for i in l:
    if i.text != '':
        print(i.text, "= ", i.get_attribute('href'))

# driver.quit()
