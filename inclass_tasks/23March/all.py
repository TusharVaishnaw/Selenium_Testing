from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait

o = ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
# driver.get("https://amazon.in")
# ele=driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
# ele.send_keys('Watch')
# ele.send_keys(Keys.ENTER)
#
# driver.get("https://demoqa.com/text-box")
# cadd=driver.find_element(By.ID,'currentAddress')
# cadd.send_keys('pratap nagar, Jaipur')
# cadd.send_keys(Keys.CONTROL,'A')
# cadd.send_keys(Keys.CONTROL,'C')
# padd=driver.find_element(By.ID,'permanentAddress')
# padd.send_keys(Keys.CONTROL,'V')

actions = ActionChains(driver)

# driver.get("https://demoqa.com/buttons")
# dc=driver.find_element(By.ID,'doubleClickBtn')
# # actions.double_click(dc).perform()
# sc = driver.find_element(By.XPATH, "//button[text()='Click Me']")
# actions.click(sc).perform()
# actions.click(sc).perform()
# actions.double_click(dc).perform()
# rc=driver.find_element(By.ID,'rightClickBtn')
# actions.context_click(rc).perform()

# driver.get("https://amazon.in")
# insta=driver.find_element(By.XPATH,"//a[@href='https://www.instagram.com/amazondotin']")
# actions.scroll_to_element(insta).pause(3).perform()
# actions.scroll_by_amount(0,10000).pause(3).perform()
# o=ScrollOrigin.from_element(insta)
# o=ScrollOrigin.from_viewport(0,300)
# actions.pause(3).scroll_from_origin(o,0,50).perform()

# ele=driver.find_element(By.XPATH,"(//a[@class='nav-a nav-a-2   nav-progressive-attribute'])[1]")
# ele2=driver.find_element(By.XPATH,"//span[text()='Your Orders']")
# actions.move_to_element(ele).pause(3).click(ele2).perform()

# driver.get("https://yonobusiness.sbi.bank.in/yonobusinesslogin")
# sleep(7)
# psw=driver.find_element(By.ID,"password")
# psw.send_keys('Password')
# eye=driver.find_element(By.XPATH,"//button[@tabindex='0']")
# actions.click_and_hold(eye).pause(4).release(eye).perform()

# driver.get("https://demoqa.com/droppable")
# d1=driver.find_element(By.ID,"draggable")
# d2=driver.find_element(By.ID,"droppable")
# sleep(3)
# actions.drag_and_drop(d1,d2).perform()


driver.get("https://google.com")
sleep(2)

# manually open 3 tabs

w1 = driver.current_window_handle
driver.switch_to.new_window()
driver.get("https://demoqa.com/droppable")
print(driver.window_handles)

driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.LINK_TEXT,"About").click()












sleep(5)
driver.quit()
