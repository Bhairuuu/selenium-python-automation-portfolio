from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import WebDriverWait


class CheckoutPage:
    """Models checkout, delivery-country selection, and order confirmation."""

    checkout_button = (By.CSS_SELECTOR, ".btn.btn-success")
    country_input = (By.ID, "country")
    india_suggestion = (
        By.XPATH,
        "//div[@class='suggestions']//a[contains(normalize-space(), 'India')]",
    )
    terms_checkbox = (By.ID, "checkbox2")
    purchase_button = (By.CSS_SELECTOR, "input[value='Purchase']")
    success_message = (By.CLASS_NAME, "alert-success")

    def __init__(self, driver: WebDriver, timeout: int = 15) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def checkout(self) -> None:
        self.wait.until(expected.element_to_be_clickable(self.checkout_button)).click()
        self.wait.until(expected.visibility_of_element_located(self.country_input))

    def complete_purchase(self, country: str = "ind") -> None:
        country_input = self.wait.until(
            expected.element_to_be_clickable(self.country_input)
        )
        country_input.clear()
        country_input.send_keys(country)

        suggestion = self.wait.until(
            expected.element_to_be_clickable(self.india_suggestion)
        )
        self.driver.execute_script("arguments[0].click();", suggestion)

        checkbox = self.wait.until(
            expected.presence_of_element_located(self.terms_checkbox)
        )
        self.driver.execute_script("arguments[0].click();", checkbox)

        purchase_button = self.wait.until(
            expected.element_to_be_clickable(self.purchase_button)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", purchase_button
        )
        self.driver.execute_script("arguments[0].click();", purchase_button)

    def confirmation_text(self) -> str:
        return self.wait.until(
            expected.visibility_of_element_located(self.success_message)
        ).text
