from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")

# Click Shop
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

# Select Blackberry
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text

    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()
        break

# Go to Cart
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

# Checkout
driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()

# Enter Country
driver.find_element(By.ID, "country").send_keys("ind")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

driver.find_element(By.LINK_TEXT, "India").click()

# Select Checkbox
#driver.find_element(By.XPATH, "//input[@type='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
# Purchase
driver.find_element(By.XPATH, "//input[@value='Purchase']").click()

# Verify Success Message
successText = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success! Thank you!" in successText

print("Test Passed")