# from selenium.webdriver.common.by import By
#
#
# class LoginPage:
#
#     def __init__(self,driver):
#         self.driver=driver
#         self.user_input=(By.ID, "username")
#         self.password=(By.NAME, "password")
#         self.sign_btn=(By.ID, "signInBtn")
#     def login(self,username,password):
#         self.driver.find_element(*self.user_input).send_keys("authorized_test_user")
#         self.driver.find_element(*self.password).send_keys("authorized_test_password")
#         self.driver.find_element(*self.sign_btn).click()


from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self,driver):
        self.driver=driver
        self.user_input=(By.ID, "username")
        self.password=(By.NAME, "password")
        self.sign_btn=(By.ID, "signInBtn")

    def login(self,username,password):

        self.driver.find_element(*self.user_input).send_keys(username)

        self.driver.find_element(*self.password).send_keys(password)

        self.driver.find_element(*self.sign_btn).click()
