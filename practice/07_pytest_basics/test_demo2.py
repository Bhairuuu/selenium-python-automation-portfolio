# you can mark(tag) tests @pytest.mark.smoke and run with -m
#you can skip tests with @pytest.mark.skip
#@pytest.mark.xfail

import pytest
@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg="hello"
    assert msg=="hi","test failed because string does not match "
    print(msg)

def test_secondCreditCard():
    a=4
    b=6

    assert a+2==6 , "Addition do not match"

@pytest.fixture()

def setup():
    print("i will be executing first")


def test_fixtureDemo(setup):
    print("i will executes steps in test_fixtureDemo method ")
