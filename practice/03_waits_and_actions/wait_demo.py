

import time
from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(5)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

count = len(results)
assert count > 0

for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a.cart-icon").click()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

#driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CLASS_NAME, "promoBtn").click()

time.sleep(8)

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

driver.quit()