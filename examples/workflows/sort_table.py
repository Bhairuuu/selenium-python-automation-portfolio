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
        original_window = driver.current_window_handle
        driver.find_element(By.LINK_TEXT, "Top Deals").click()

        wait.until(expected.number_of_windows_to_be(2))
        deals_window = next(
            handle for handle in driver.window_handles if handle != original_window
        )
        driver.switch_to.window(deals_window)

        wait.until(
            expected.element_to_be_clickable(
                (By.XPATH, "//span[normalize-space()='Veg/fruit name']")
            )
        ).click()
        names = [
            element.text
            for element in wait.until(
                expected.visibility_of_all_elements_located((By.XPATH, "//tr/td[1]"))
            )
        ]

        assert names == sorted(names), "Table is not sorted alphabetically."
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
