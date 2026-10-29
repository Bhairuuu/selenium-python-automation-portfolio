import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/client")

wait = WebDriverWait(driver, 10)

# Click forgot password
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Forgot Password?"))).click()

# Enter email
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']"))).send_keys("demo@gmail.com")

# Enter new password
driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("hello@123")

# Click save button
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()

time.sleep(5)