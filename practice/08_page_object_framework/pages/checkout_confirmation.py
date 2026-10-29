# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support import expected_conditions
# # from selenium.webdriver.support.wait import WebDriverWait
# #
# #
# # class Checkout_Confirmation:
# #
# #     def __init__(self,driver):
# #         self.driver = driver
# #         self.country_input=(By.ID,"country")
# #         self.country_option=(By.LINK_TEXT, "India")
# #         self.checkbox=(By.XPATH ,"//label[@for='checkbox2']")
# #         self.submit_button=(By.XPATH ,"//input[@value='Purchase']")
# #         self.success_message=(By.CLASS_NAME,"alert-success" )
# #     def checkout(self):
# #
# #         # Checkout
# #         self.driver.find_element(*self.country_input).click()
# #
# #
# #
# #     def enter_delivery_address(self,CountryName):
# #
# #         # Enter Country
# #         self.driver.find_element(*self.country_input).send_keys(CountryName)
# #
# #         wait = WebDriverWait(self.driver, 10)
# #         wait.until(expected_conditions.presence_of_element_located(self.country_option))
# #
# #         self.driver.find_element(*self.country_option).click()
# #
# #         # Select Checkbox
# #         # driver.find_element(By.XPATH, "//input[@type='checkbox checkbox-primary']").click()
# #         self.driver.find_element(*self.checkbox).click()
# #         # Purchase
# #         self.driver.find_element(*self.submit_button).click()
# #
# #
# #
# #     def validate_order(self):
# #         successText = self.driver.find_element(*self.success_message).text
# #
# #         assert "Success! Thank you!" in successText
# #
# #         print("Test Passed")
#
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class Checkout_Confirmation:
#
#     def __init__(self, driver):
#         self.driver = driver
#
#         # Checkout button in Cart page
#         self.checkout_button = (
#             By.CSS_SELECTOR,
#             ".btn.btn-success"
#         )
#
#         # Country input in Checkout page
#         self.country_input = (
#             By.ID,
#             "country"
#         )
#
#         self.country_option = (
#             By.LINK_TEXT,
#             "India"
#         )
#
#         # self.checkbox = (
#         #     By.XPATH,
#             "//label[@for='checkbox2']"
#         )
#
#         self.submit_button = (
#             By.XPATH,
#             "//input[@value='Purchase']"
#         )
#
#         self.success_message = (
#             By.CLASS_NAME,
#             "alert-success"
#         )
#
#     def checkout(self):
#
#         wait = WebDriverWait(self.driver, 10)
#
#         # Click Checkout button
#         checkout_button = wait.until(
#             EC.element_to_be_clickable(self.checkout_button)
#         )
#
#         checkout_button.click()
#
#         # Wait until checkout page loads
#         wait.until(
#             EC.visibility_of_element_located(self.country_input)
#         )
#
#     def enter_delivery_address(self, country_name):
#
#         wait = WebDriverWait(self.driver, 10)
#
#         # Find country field
#         country = wait.until(
#             EC.element_to_be_clickable(self.country_input)
#         )
#
#         # Enter country
#         country.send_keys(country_name)
#
#         # Select India
#         india = wait.until(
#             EC.element_to_be_clickable(self.country_option)
#         )
#
#         india.click()
#
#         # Select checkbox
#         checkbox = wait.until(
#             EC.element_to_be_clickable(self.checkbox)
#         )
#
#         checkbox.click()
#
#         # Click Purchase
#         purchase_button = wait.until(
#             EC.element_to_be_clickable(self.submit_button)
#         )
#
#         purchase_button.click()
#
#     def validate_order(self):
#
#         wait = WebDriverWait(self.driver, 15)
#
#         success_text = wait.until(
#             EC.visibility_of_element_located(self.success_message)
#         ).text
#
#         assert "Success! Thank you!" in success_text
#
#         print("Test Passed")





# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# class Checkout_Confirmation:
#
#     def __init__(self,driver):
#
#         self.driver = driver
#
#         self.checkout_button=(By.CSS_SELECTOR,".btn.btn-success")
#
#         self.country_input=(By.ID,"country")
#
#         self.country_option=(By.LINK_TEXT,"India")
#
#         # Changed from label XPath to actual checkbox
#         self.checkbox=(By.ID,"checkbox2")
#
#         self.submit_button=(By.XPATH,"//input[@value='Purchase']")
#
#         self.success_message=(By.CLASS_NAME,"alert-success")
#
#
#     def checkout(self):
#
#         wait = WebDriverWait(self.driver,10)
#
#         checkout_button = wait.until(
#             expected_conditions.element_to_be_clickable(
#                 self.checkout_button
#             )
#         )
#
#         checkout_button.click()
#
#
#         wait.until(
#             expected_conditions.visibility_of_element_located(
#                 self.country_input
#             )
#         )
#
#
#     def enter_delivery_address(self,CountryName):
#
#         wait = WebDriverWait(self.driver,10)
#
#
#         # Enter Country
#         country = wait.until(
#             expected_conditions.visibility_of_element_located(
#                 self.country_input
#             )
#         )
#
#         country.clear()
#
#         country.send_keys(CountryName)
#
#
#         # Select India
#         india = wait.until(
#             expected_conditions.element_to_be_clickable(
#                 self.country_option
#             )
#         )
#
#         india.click()
#
#
#         # Select Checkbox
#         checkbox = wait.until(
#             expected_conditions.presence_of_element_located(
#                 self.checkbox
#             )
#         )
#
#         # JavaScript click to avoid click intercepted error
#         self.driver.execute_script(
#             "arguments[0].click();",
#             checkbox
#         )
#
#
#         # Purchase
#         purchase_button = wait.until(
#             expected_conditions.element_to_be_clickable(
#                 self.submit_button
#             )
#         )
#
#         purchase_button.click()
#
#
#     def validate_order(self):
#
#         wait = WebDriverWait(self.driver,15)
#
#         successText = wait.until(
#             expected_conditions.visibility_of_element_located(
#                 self.success_message
#             )
#         ).text
#
#
#         assert "Success! Thank you!" in successText
#
#         print("Test Passed")



from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Checkout_Confirmation:

    def __init__(self,driver):

        self.driver = driver

        self.checkout_button=(By.CSS_SELECTOR,".btn.btn-success")

        self.country_input=(By.ID,"country")

        #self.country_option=(By.XPATH,"//div[@class='suggestions']/ul/li/a")
        self.country_option = (
            By.XPATH,
            "//div[@class='suggestions']/ul/li/a[contains(text(),'India')]"
        )
        self.checkbox=(By.ID,"checkbox2")

        self.submit_button=(By.XPATH,"//input[@value='Purchase']")

        self.success_message=(By.CLASS_NAME,"alert-success")


    def checkout(self):

        wait = WebDriverWait(self.driver,10)

        checkout_button = wait.until(
            expected_conditions.element_to_be_clickable(
                self.checkout_button
            )
        )

        checkout_button.click()


        wait.until(
            expected_conditions.visibility_of_element_located(
                self.country_input
            )
        )


    def enter_delivery_address(self,CountryName):

        wait = WebDriverWait(self.driver,15)


        # Enter Country
        country = wait.until(
            expected_conditions.visibility_of_element_located(
                self.country_input
            )
        )

        country.clear()

        country.send_keys(CountryName)


        # Wait for country suggestion
        india = wait.until(
            expected_conditions.visibility_of_element_located(
                self.country_option
            )
        )


        # Click India suggestion using JavaScript
        self.driver.execute_script(
            "arguments[0].click();",
            india
        )


        # Wait for suggestion dropdown to disappear
        wait.until(
            expected_conditions.invisibility_of_element_located(
                (By.CLASS_NAME,"suggestions")
            )
        )


        # Select Checkbox
        checkbox = wait.until(
            expected_conditions.presence_of_element_located(
                self.checkbox
            )
        )


        self.driver.execute_script(
            "arguments[0].click();",
            checkbox
        )


        # Find Purchase button
        purchase_button = wait.until(
            expected_conditions.presence_of_element_located(
                self.submit_button
            )
        )


        # Scroll Purchase button into view
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            purchase_button
        )


        # Click Purchase using JavaScript
        self.driver.execute_script(
            "arguments[0].click();",
            purchase_button
        )


    def validate_order(self):

        wait = WebDriverWait(self.driver,15)

        successText = wait.until(
            expected_conditions.visibility_of_element_located(
                self.success_message
            )
        ).text


        assert "Success! Thank you!" in successText

        print("Test Passed")