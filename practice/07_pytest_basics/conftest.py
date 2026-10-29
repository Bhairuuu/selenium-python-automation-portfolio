import pytest


@pytest.fixture()

def setup():
    print("i will be executing first")
    yield
    print("i will execute last")

@pytest.fixture()
def dataLoad():
    print("user profile data in being created")
    return ["bhairu","'katrat","136"]

@pytest.fixture(params=["chrome","firefox","IE"])
def crossBrowser(request):
    return request.param


@pytest.fixture(params=[("chrome","Bhairu"),"firefox",("IE","Katart")])
def crossBrowsers(request):
    return request.param