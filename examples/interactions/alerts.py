from selenium import webdriver
from selenium.webdriver.common.by import By

PRACTICE_URL = "https://rahulshettyacademy.com/AutomationPractice/"


def main() -> None:
    driver = webdriver.Chrome()
    try:
        driver.get(PRACTICE_URL)
        name = "Test User"
        driver.find_element(By.ID, "name").send_keys(name)
        driver.find_element(By.ID, "alertbtn").click()

        alert = driver.switch_to.alert
        assert name in alert.text
        alert.accept()
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
