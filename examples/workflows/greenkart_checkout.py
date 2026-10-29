from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import WebDriverWait

PRACTICE_URL = "https://rahulshettyacademy.com/seleniumPractise/#/"


def main() -> None:
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    try:
        driver.get(PRACTICE_URL)
        driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")

        products = wait.until(
            expected.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".products > .product")
            )
        )
        assert products, "No products matched the search."

        for product in products:
            product.find_element(By.TAG_NAME, "button").click()

        driver.find_element(By.CSS_SELECTOR, "a.cart-icon").click()
        wait.until(
            expected.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='PROCEED TO CHECKOUT']")
            )
        ).click()

        prices = wait.until(
            expected.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "tr td:nth-child(5) p")
            )
        )
        calculated_total = sum(int(price.text) for price in prices)
        displayed_total = int(driver.find_element(By.ID, "totAmt").text)
        assert calculated_total == displayed_total

        driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys(
            "rahulshettyacademy"
        )
        driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
        promo_message = wait.until(
            expected.visibility_of_element_located((By.CSS_SELECTOR, ".promoInfo"))
        )
        print(promo_message.text)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
