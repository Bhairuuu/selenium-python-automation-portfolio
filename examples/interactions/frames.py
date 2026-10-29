from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import WebDriverWait

PRACTICE_URL = "https://the-internet.herokuapp.com/iframe"


def main() -> None:
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    try:
        driver.get(PRACTICE_URL)
        wait.until(expected.frame_to_be_available_and_switch_to_it((By.ID, "mce_0_ifr")))

        editor = wait.until(expected.visibility_of_element_located((By.ID, "tinymce")))
        editor.clear()
        editor.send_keys("Updated by Selenium")
        assert editor.text == "Updated by Selenium"

        driver.switch_to.default_content()
        assert driver.find_element(By.TAG_NAME, "h3").text == "An iFrame containing the TinyMCE WYSIWYG Editor"
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
