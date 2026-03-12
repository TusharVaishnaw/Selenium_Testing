# from time import sleep
# #
# # from selenium.webdriver import Edge
# #
# # driver = Edge()
# # sleep(5)
# """
# selenium is a pakacge
# webdriver a module
# and chrome and chromeoptions are classes inside that
# """
#
# from selenium.webdriver import Chrome, ChromeOptions
# o = ChromeOptions()
# # o.add_experimental_option("detach", True)  # keep browser open after script ends
# driver = Chrome(options=o)
#
# '''browser window size options'''
# # to open webpage
# # driver.get("http://google.com")
# # # to maximise
# # driver.maximize_window()
# # driver.fullscreen_window()
# # driver.minimize_window()
#
# # driver.get("http://myntra.com")
#
# # to maximise
# # driver.maximize_window()
# # driver.minimize_window()
# # sleep(1)
# # driver.fullscreen_window()
# # sleep(1)
#
# '''website info fetch methods'''
# driver.get("http://demoqa.com")
# title=driver.title
# print(title)
# print(driver.current_url)
# # print(driver.page_source)
#
# '''close vs quit
# close- just closes thge tab while quit exits the browser window
# '''
# sleep(2)
# driver.close()
# sleep(2)
# driver.quit()
#
from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.maximize_window()
driver.get("https://amazon.com")
sleep(5)
driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.quit()
