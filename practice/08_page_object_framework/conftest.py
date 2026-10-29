import pytest
from pygments.lexer import default
from selenium import webdriver
from selenium.webdriver.ie.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store",default="chrome",help="browser selection"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name=request.config.getoption("browser_name")
    service_obj=Service()
    if browser_name=="chrome":
        driver = webdriver.Chrome(service=service_obj)
        driver.implicitly_wait(4)
    elif browser_name=="firefox":
        driver = webdriver.Firefox(service=service_obj)
        driver.implicitly_wait(4)
    yield driver
