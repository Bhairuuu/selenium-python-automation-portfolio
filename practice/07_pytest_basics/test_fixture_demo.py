import pytest



@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("i will executes steps in test_fixtureDemo method ")
    def test_fixtureDemo1(self):
        print("i will executes steps in test_fixtureDemo1 method ")

    def test_fixtureDemo2(self):
            print("i will executes steps in test_fixtureDemo2 method ")
    def test_fixtureDemo3(self):
        print("i will executes steps in test_fixtureDemo3 method ")

    def test_fixtureDemo4(self):
        print("i will executes steps in test_fixtureDemo method ")