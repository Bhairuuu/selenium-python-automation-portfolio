# from selenium.webdriver.common.by import By
#
# from PageObject.checkout_confirmation import Checkout_Confirmation
#
#
# class ShopPage:
#
#     def __init__(self, driver):
#         self.driver = driver
#
#         self.shop_link = (By.CSS_SELECTOR, "a[href*='shop']")
#         self.product_cards = (By.XPATH, "//div[@class='card h-100']")
#         self.checkoutBtn = (By.CSS_SELECTOR, "a[class*='btn-primary']")
#
#     def add_product_to_cart(self, product_name):
#
#         self.driver.find_element(*self.shop_link).click()
#
#         products = self.driver.find_elements(*self.product_cards)
#
#         for product in products:
#             productName = product.find_element(By.XPATH, "div/h4/a").text
#
#             if productName == product_name:
#                 product.find_element(By.XPATH, "div/button").click()
#                 break
#
#     def go_to_cart(self):
#         self.driver.find_element(*self.checkoutBtn).click()
#         checkout_confirmation=Checkout_Confirmation(self.driver)
#         return checkout_confirmation




from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.checkout_confirmation import Checkout_Confirmation


class ShopPage:

    def __init__(self, driver):
        self.driver = driver

        self.shop_link = (By.CSS_SELECTOR, "a[href*='shop']")
        self.product_cards = (By.XPATH, "//div[@class='card h-100']")
        self.checkoutBtn = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def add_product_to_cart(self, product_name):

        wait = WebDriverWait(self.driver,10)

        # Open Shop Page
        wait.until(
            expected_conditions.element_to_be_clickable(
                self.shop_link
            )
        ).click()

        # Get all products
        products = wait.until(
            expected_conditions.presence_of_all_elements_located(
                self.product_cards
            )
        )

        for product in products:

            productName = product.find_element(
                By.XPATH,
                "div/h4/a"
            ).text

            if productName == product_name:

                product.find_element(
                    By.XPATH,
                    "div/button"
                ).click()

                break


    def go_to_cart(self):

        wait = WebDriverWait(self.driver,10)

        wait.until(
            expected_conditions.element_to_be_clickable(
                self.checkoutBtn
            )
        ).click()

        checkout_confirmation = Checkout_Confirmation(
            self.driver
        )

        return checkout_confirmation
