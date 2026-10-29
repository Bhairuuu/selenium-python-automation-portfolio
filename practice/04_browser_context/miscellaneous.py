from selenium import webdriver

# Create Chrome options
chrome_options = webdriver.ChromeOptions()

# Run browser in headless mode
chrome_options.add_argument("--headless")

# Ignore SSL certificate errors
chrome_options.add_argument("--ignore-certificate-errors")

# Launch Chrome
driver = webdriver.Chrome(options=chrome_options)

# Open website
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Scroll to bottom of page
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")

# Take screenshot
driver.get_screenshot_as_file("screen.png")

# Close browser
driver.quit()