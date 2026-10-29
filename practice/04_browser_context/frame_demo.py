import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/windows")
driver.switch_to.frame("mce-0-ifr")
driver.find_element(By.ID,"tynemce").clear()
driver.find_element(By.ID,"tynemce").send_keys("I am Bhairu Katrat")
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h3"))