from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
o = ChromeOptions()
o.add_experimental_option('detach', True)
o.add_experimental_option("prefs",{"safebrowsing.enabled":True})
o.add_argument("--disable-notifications")
driver = Chrome(options=o)

driver.implicitly_wait(10)
# actions = ActionChains(driver)

# driver.get(r"C:\Users\ASUS\Desktop\CG_T\sel\pythonProject\24Mar\1.html")
# in1= driver.find_element(By.ID,'in1')
# in1.send_keys('hello1')
#
#
# # driver.switch_to.frame(0)
# # driver.switch_to.frame("pagetwo")
# # driver.switch_to.frame("frame1")
# pg2=driver.find_element(By.XPATH,"//iframe[@src='page2.html']")
# driver.switch_to.frame(pg2)
# in2=driver.find_element(By.ID,'in2')
# in2.send_keys('hello2')


# driver.switch_to.frame(0)
# driver.switch_to.frame("page3")
# driver.switch_to.frame("frame2")
# pg3=driver.find_element(By.XPATH,"//iframe[@src='page3.html']")
# driver.switch_to.frame(pg3)
# in3=driver.find_element(By.ID,'in3')
# in3.send_keys('hello3')
#
# sleep(2)
# driver.switch_to.parent_frame()
# in2.clear()
# in2.send_keys('backfrom3')
#
# driver.switch_to.parent_frame()
# in1.clear()
# in1.send_keys('back')
# sleep(1)
# driver.switch_to.frame(0)
# driver.switch_to.frame(0)
# in3.clear()
# in3.send_keys('hueheu')
# driver.switch_to.default_content()
# in1.send_keys('final')

# driver.get("https://testautomationpractice.blogspot.com/")
# a1=driver.find_element(By.ID,"alertBtn")
# a1.click()
# sleep(1)
# a1=driver.switch_to.alert.accept()
# # a1=driver.switch_to.alert.dismiss()
#
#
# a2=driver.find_element(By.ID,"confirmBtn")
# a2.click()
# sleep(1)
# a2=driver.switch_to.alert.dismiss()
#
# a3=driver.find_element(By.ID,"promptBtn")
# a3.click()
# sleep(1)
# a3=driver.switch_to.alert
# a3.send_keys('Tushar Vaishnaw')
# sleep(1)
# a3.accept()

# driver.get("https://demoqa.com/upload-download")
# driver.find_element(By.ID,"downloadButton").click()
#
# driver.find_element(By.ID,"uploadFile").send_keys(r"T:\Downloadz\Weekly_Assessment_2.md")

# driver.get("https://www.python.org/downloads/")
# driver.find_element(By.XPATH,"//a[text()='Download Python install manager']").click()

# driver.get("https://www.irctc.co.in/nget/train-search")
# driver.find_element(By.XPATH,"//input[@class='ng-tns-c69-9 ui-inputtext ui-widget ui-state-default ui-corner-all ng-star-inserted']").click()
# driver.find_element(By.LINK_TEXT,"28").click()

driver.get("https://demoqa.com/automation-practice-form")
driver.find_element(By.ID,"dateOfBirthInput").click()
sleep(1)
driver.find_element(By.XPATH,"//div[text()='28']").click()


sleep(10)
driver.quit()




