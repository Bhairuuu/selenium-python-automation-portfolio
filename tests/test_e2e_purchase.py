import json
from pathlib import Path

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from ui_automation.pages.login_page import LoginPage
from ui_automation.pages.shop_page import ShopPage

TEST_DATA = Path(__file__).parent / "data" / "purchase_cases.json"
PURCHASE_CASES = json.loads(TEST_DATA.read_text(encoding="utf-8"))


@pytest.mark.e2e
@pytest.mark.parametrize("case", PURCHASE_CASES, ids=lambda case: case["product"])
def test_customer_can_purchase_a_product(
    driver: WebDriver, test_credentials: tuple[str, str], case: dict[str, str]
) -> None:
    """Completes a data-driven purchase flow in the training application."""
    username, password = test_credentials
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    LoginPage(driver).login(username, password)
    shop = ShopPage(driver)
    shop.add_product_to_cart(case["product"])
    checkout = shop.go_to_cart()
    checkout.checkout()
    checkout.complete_purchase()

    assert "Success! Thank you!" in checkout.confirmation_text()
