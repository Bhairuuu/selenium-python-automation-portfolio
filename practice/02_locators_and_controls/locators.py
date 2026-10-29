import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#driver.get("https://rahulshettyacademy.com/angularpractice/")

# driver.find_element(By.NAME, "email").send_keys("bhairukatrat7085@gmail.com")
# driver.find_element(By.ID, "exampleInputPassword1").send_keys("1234")
# driver.find_element(By.ID, "exampleCheck1").click()
#
# # xpath selectors
# # //tagname[@attribute='value']-> // input[@type='submit']
# driver.find_element(By.XPATH, "//input[@type='submit']").click()
# driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("hello")
#
# # css selectors
# #"tagname[@attribute='value']"-> "input[type='submit']"
# driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Bhairu")
# driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
#
# message = driver.find_element(By.CLASS_NAME, "alert-success").text
# print(message)
#
# assert "Success" in message

# static dropdown

dropdown=select(driver.find_element( By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
dropdown.select_by_value()
time.sleep(10)

