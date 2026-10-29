import time

from selenium import webdriver

driver = webdriver.Chrome()


driver.get("https://Gmail.com")
driver.maximize_window()
print("title:",( driver.title))
print(driver.current_url)


time.sleep(2)

# import time
#
# from selenium import webdriver
#
# driver = webdriver.Firefox()
#
#
# driver.get("https://Gmail.com")
# driver.maximize_window()
# print("title:",( driver.title))
# print(driver.current_url)
#
#
# time.sleep(2)