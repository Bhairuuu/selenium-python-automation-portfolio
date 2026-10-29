from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import WebDriverWait

from ui_automation.pages.checkout_page import CheckoutPage


class ShopPage:
    """Models product selection and navigation to the cart."""

    shop_link = (By.CSS_SELECTOR, "a[href*='shop']")
    product_cards = (By.CSS_SELECTOR, ".card.h-100")
    cart_link = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def add_product_to_cart(self, product_name: str) -> None:
        self.wait.until(expected.element_to_be_clickable(self.shop_link)).click()
        product_cards = self.wait.until(
            expected.presence_of_all_elements_located(self.product_cards)
        )

        for product_card in product_cards:
            name = product_card.find_element(By.CSS_SELECTOR, "h4 a").text
            if name == product_name:
                product_card.find_element(By.CSS_SELECTOR, "button").click()
                return

        raise AssertionError(f"Product '{product_name}' was not found.")

    def go_to_cart(self) -> CheckoutPage:
        self.wait.until(expected.element_to_be_clickable(self.cart_link)).click()
        return CheckoutPage(self.driver)
