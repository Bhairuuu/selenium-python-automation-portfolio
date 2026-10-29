from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Encapsulates the login form for the training application."""

    username_input = (By.ID, "username")
    password_input = (By.NAME, "password")
    sign_in_button = (By.ID, "signInBtn")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def login(self, username: str, password: str) -> None:
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.sign_in_button).click()
