from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch browser
driver = webdriver.Chrome()

browserSortedList = []

# Open GreenKart website
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# Click on Top Deals
driver.find_element(By.LINK_TEXT, "Top Deals").click()

# Switch to the new window
windows = driver.window_handles
driver.switch_to.window(windows[1])

# Click on Veg/Fruit Name column to sort
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# Get all vegetable names from first column
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")

# Store names in a list
for ele in veggieWebElements:
    browserSortedList.append(ele.text)

# Copy the browser list
originalBrowserSortedList = browserSortedList.copy()

# Sort the copied list using Python
browserSortedList.sort()

# Compare both lists
assert browserSortedList == originalBrowserSortedList

print("Sorting is working correctly!")

driver.quit()