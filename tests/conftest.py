import os
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


def load_local_env() -> None:
    env_file = Path(__file__).resolve().parent.parent / ".env"
    if not env_file.exists():
        return

    for line in env_file.read_text(encoding="utf-8").splitlines():
        key, separator, value = line.partition("=")
        if separator and key and not key.lstrip().startswith("#"):
            os.environ.setdefault(key.strip(), value.strip())


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=("chrome", "firefox"),
        help="Browser used for UI tests.",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run the selected browser without a visible window.",
    )


@pytest.fixture
def driver(request: pytest.FixtureRequest) -> WebDriver:
    browser_name = request.config.getoption("browser")
    headless = request.config.getoption("headless")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        browser = webdriver.Chrome(options=options)
    else:
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        browser = webdriver.Firefox(options=options)

    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope="session")
def test_credentials() -> tuple[str, str]:
    load_local_env()
    username = os.getenv("TEST_USERNAME")
    password = os.getenv("TEST_PASSWORD")

    if not username or not password:
        pytest.skip(
            "Set TEST_USERNAME and TEST_PASSWORD in a local .env file to run e2e tests."
        )

    return username, password
