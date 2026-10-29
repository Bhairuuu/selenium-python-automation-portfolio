from selenium import webdriver
from selenium.webdriver.common.by import By

PRACTICE_URL = "https://rahulshettyacademy.com/AutomationPractice/"


def main() -> None:
    driver = webdriver.Chrome()
    try:
        driver.get(PRACTICE_URL)
        radio_button = driver.find_element(
            By.CSS_SELECTOR, "input.radioButton[value='radio2']"
        )
        radio_button.click()
        assert radio_button.is_selected()

        checkbox = driver.find_element(By.CSS_SELECTOR, "input[value='option2']")
        checkbox.click()
        assert checkbox.is_selected()
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
