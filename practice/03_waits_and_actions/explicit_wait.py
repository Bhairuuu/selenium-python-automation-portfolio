

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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

# sum validations
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")

calculated_sum = sum(int(price.text) for price in prices)

print(calculated_sum)

TotalAmount = int(driver.find_element(By.ID, "totAmt").text)

assert calculated_sum == TotalAmount


#driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CLASS_NAME, "promoBtn").click()


wait= WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

driver.quit()