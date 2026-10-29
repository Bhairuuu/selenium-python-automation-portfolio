from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import WebDriverWait

PRACTICE_URL = "https://rahulshettyacademy.com/AutomationPractice/"


def main() -> None:
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    try:
        driver.get(PRACTICE_URL)
        driver.maximize_window()

        hover_target = wait.until(
            expected.visibility_of_element_located((By.ID, "mousehover"))
        )
        ActionChains(driver).move_to_element(hover_target).perform()
        wait.until(expected.element_to_be_clickable((By.LINK_TEXT, "Top"))).click()
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
