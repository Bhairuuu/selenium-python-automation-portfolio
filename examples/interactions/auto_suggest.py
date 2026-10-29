from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import WebDriverWait

PRACTICE_URL = "https://rahulshettyacademy.com/dropdownsPractise/"


def main() -> None:
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    try:
        driver.get(PRACTICE_URL)
        input_field = driver.find_element(By.ID, "autosuggest")
        input_field.send_keys("ind")

        options = wait.until(
            expected.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, "li.ui-menu-item a")
            )
        )
        next(option for option in options if option.text == "India").click()
        assert input_field.get_attribute("value") == "India"
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
