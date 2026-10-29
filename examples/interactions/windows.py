from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import WebDriverWait

PRACTICE_URL = "https://the-internet.herokuapp.com/windows"


def main() -> None:
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    try:
        driver.get(PRACTICE_URL)
        original_window = driver.current_window_handle
        driver.find_element(By.LINK_TEXT, "Click Here").click()

        wait.until(expected.number_of_windows_to_be(2))
        new_window = next(
            handle for handle in driver.window_handles if handle != original_window
        )
        driver.switch_to.window(new_window)
        assert driver.find_element(By.TAG_NAME, "h3").text == "New Window"

        driver.switch_to.window(original_window)
        assert driver.find_element(By.TAG_NAME, "h3").text == "Opening a new window"
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
