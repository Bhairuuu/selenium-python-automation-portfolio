from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Handling checkboxes
# checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
#
# print("Number of checkboxes:", len(checkboxes))
#
# for checkbox in checkboxes:
#     if checkbox.get_attribute("value") == "option2":
#         checkbox.click()
#         assert checkbox.is_selected()
#         print("Option2 checkbox selected")
#         break

# Handling radio buttons
radiobtns = driver.find_elements(By.CLASS_NAME, "radioButton")
radiobtns[2].click()
assert radiobtns[2].is_selected()

# with loop
for radiobtn in radiobtns:
    if radiobtn.get_attribute("value") == "radio2":
        radiobtn.click()
        assert radiobtn.is_selected()
        print("Radio2 selected")
        break

# #without loop
# assert driver.find_element(By.ID,"displayed-text" ).is_displayed()
# driver.find_element(By.ID,"hide-textbox").click()
# assert not driver.find_element(By.ID,"displayed-text" ).is_displayed()


driver.quit()