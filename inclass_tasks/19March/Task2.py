from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
'''forms demoqa'''
driver.get('https://demoqa.com/automation-practice-form')
driver.find_element(By.XPATH,"//input[@id='firstName']").send_keys('Tushar')
driver.find_element(By.XPATH,"//input[@id='lastName']").send_keys('Vaishnaw')
driver.find_element(By.XPATH,"//input[@id='userEmail']").send_keys('tvw11@gmail.com')
driver.find_element(By.XPATH,"//input[@id='gender-radio-1']").click()
driver.find_element(By.XPATH,"//input[@id='userNumber']").send_keys('9509494140')

driver.find_element(By.XPATH,"//input[@id='dateOfBirthInput']").click()
driver.find_element(By.XPATH,"//div[@aria-label='Choose Wednesday, March 11th, 2026']").click()


d1=(driver.find_element(By.XPATH,"//input[@id='subjectsInput']"))
d1.send_keys('Maths')
d1.send_keys(Keys.ENTER)
# d2=(driver.find_element(By.XPATH,"//input[@id='subjectsInput']"))
d1.send_keys('English')
d1.send_keys(Keys.ENTER)

driver.find_element(By.XPATH,"//input[@id='hobbies-checkbox-1']").click()
driver.find_element(By.XPATH,"//input[@id='hobbies-checkbox-2']").click()
driver.find_element(By.XPATH,"//input[@id='hobbies-checkbox-3']").click()
driver.find_element(By.XPATH,"//input[@id='uploadPicture']").send_keys(r"C:\Users\ASUS\Pictures\Screenshots\Screenshot 2024-04-20 151135.png")
driver.find_element(By.XPATH,"//textarea[@id='currentAddress']").send_keys('Prapta Nagar, Jaipur, Rajasthan(302033)')

dd1=driver.find_element(By.XPATH,"//input[@id='react-select-3-input']")
dd1.send_keys('Rajasthan')
dd1.send_keys(Keys.ENTER)
dd2=driver.find_element(By.XPATH,"//input[@id='react-select-4-input']")
dd2.send_keys('Jaipur')
dd2.send_keys(Keys.ENTER)
driver.find_element(By.XPATH,"//button[@id='submit']").click()



# driver.quit()
