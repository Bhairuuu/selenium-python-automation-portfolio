# from subprocess import check_output
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
# from PageObject.login import LoginPage
# from PageObject.shopPage import ShopPage
#
#
# def test_e2e(browserInstance):
#     driver = browserInstance
#     driver.get("https://rahulshettyacademy.com/loginpagePractise/")
import json
from pathlib import Path

import pytest

#     loginPage=LoginPage(driver)
#     loginPage.login()
#
#     # Click Shop
#     shopPage = ShopPage(driver)

#     # Select Blackberry
#
#     shopPage.add_product_to_cart("Blackberry")

#     checkout_confirmation=shopPage.go_to_cart()

#     checkout_confirmation.checkout()

#     checkout_confirmation.enter_delivery_address("ind")

#     checkout_confirmation.validate_order()
#
#     # Go to Cart
#
#     shopPage.go_to_cart()
#     driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()
#
#     # Checkout
#
#
#     # Enter Country
#     driver.find_element(By.ID, "country").send_keys("ind")
#
#     wait = WebDriverWait(driver, 10)
#     wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
#
#     driver.find_element(By.LINK_TEXT, "India").click()
#
#     # Select Checkbox
#     # driver.find_element(By.XPATH, "//input[@type='checkbox checkbox-primary']").click()
#     driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
#     # Purchase
#     driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
#
#     # Verify Success Message
#     successText = driver.find_element(By.CLASS_NAME, "alert-success").text
#
#     assert "Success! Thank you!" in successText
#
#     print("Test Passed")


# from PageObject.login import LoginPage
# from PageObject.shopPage import ShopPage
#
# test_data_path='D:\\Testing\\Data\\test_e2eTestFramework.json'
# with open(test_data_path) as f :
#     test_data=json.load(f)
#     test_list=test_data["data"]
#
# @pytest.mark.parametrize("test_list_item",test_list)
#
# def test_e2e(browserInstance,test_list_item):
#
#
#     driver = browserInstance
#
# # Open website
#     driver.get("https://rahulshettyacademy.com/loginpagePractise/")
#
# # Login
#     loginPage = LoginPage(driver)
#     loginPage.login(test_list_item["userEmail"],test_list_item["userPassword"])
#
#     # Add product
#     shopPage = ShopPage(driver)
#     shopPage.add_product_to_cart(test_list_item["product"])
#
#     # Go to cart
#     checkout_confirmation = shopPage.go_to_cart()
#
#     # Click checkout button
#     checkout_confirmation.checkout()
#
#     # Enter country and complete purchase
#     checkout_confirmation.enter_delivery_address("ind")
#
#     # Validate order
#     checkout_confirmation.validate_order()



import json
import pytest

from pages.login import LoginPage
from pages.shop_page import ShopPage


test_data_path = Path(__file__).parent / "data" / "test_e2eTestFramework.json"


with open(test_data_path) as f:

    test_data=json.load(f)

    test_list=test_data["data"]


@pytest.mark.parametrize(
    "test_list_item",
    test_list
)

def test_e2e(browserInstance,test_list_item):


    driver = browserInstance


    # Open website
    driver.get(
        "https://rahulshettyacademy.com/loginpagePractise/"
    )


    # Login
    loginPage = LoginPage(driver)

    loginPage.login(
        test_list_item["userEmail"],
        test_list_item["userPassword"]
    )


    # Add product
    shopPage = ShopPage(driver)

    shopPage.add_product_to_cart(
        test_list_item["product"]
    )


    # Go to cart
    checkout_confirmation = shopPage.go_to_cart()


    # Click checkout button
    checkout_confirmation.checkout()


    # Enter country and complete purchase
    checkout_confirmation.enter_delivery_address(
        "ind"
    )


    # Validate order
    checkout_confirmation.validate_order()
