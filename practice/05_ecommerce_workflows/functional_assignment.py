import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Expected products
expected_list = [
    "Cucumber - 1 Kg",
    "Raspberry - 1/4 Kg",
    "Strawberry - 1/4 Kg"
]

# List to store products found on the webpage
actual_list = []

# Launch Chrome
driver = webdriver.Chrome()
driver.implicitly_wait(5)

# Open website
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# Search for products containing "ber"
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(5)

# Get all displayed products
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

# Verify at least one product is displayed
assert len(results) > 0

# Store product names and click Add to Cart
for result in results:
    product_name = result.find_element(By.TAG_NAME, "h4").text
    actual_list.append(product_name)

    result.find_element(By.XPATH, "div/button").click()

# Print both lists
print("Expected List:", expected_list)
print("Actual List  :", actual_list)

# Verify both lists are the same
assert expected_list == actual_list

print("✅ Product names matched successfully!")

# Open cart
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


# Close browser
driver.quit()