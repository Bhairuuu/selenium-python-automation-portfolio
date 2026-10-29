from selenium import webdriver

PRACTICE_URL = "https://rahulshettyacademy.com/angularpractice/"


def main() -> None:
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--headless=new")
    options.add_argument("--ignore-certificate-errors")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(PRACTICE_URL)
        print(driver.title)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
