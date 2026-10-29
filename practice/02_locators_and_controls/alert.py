import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name="Bhairu"
driver.find_element(By.ID,"name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert= driver.switch_to.alert
alertText= alert.text
print(alertText)
assert name in alertText
alert.accept()
#alert.dismiss()
time.sleep(3)