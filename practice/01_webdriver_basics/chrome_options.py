from selenium import webdriver

# Create Chrome options
chrome_options = webdriver.ChromeOptions()
#maximize   window
chrome_options.add_argument("--start-maximized")

# Run browser in headless mode
chrome_options.add_argument("--headless")

# Ignore SSL certificate errors
chrome_options.add_argument("--ignore-certificate-errors")


# Launch Chrome
driver = webdriver.Chrome(options=chrome_options)

# Open website
driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)
