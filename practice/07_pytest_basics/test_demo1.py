# any pytest file start with test_  OR end with test_
# pytest method names start with test
#any code should wrapped in method only
# method name should have sense
# -k stands for method name  execution
#-s logs in output
#-v stands for more info metadata
#for running specific file use py.test <file name>
# you can mark(tag) tests @pytest.mark.smoke and run with -m
#you can skip tests with @pytest.mark.skip
#@pytest.mark.xfail
# fixtures are used as setup and tear down methods for test cases- conftest file to generalize fixture and make it available to
#all test cases (fixture name into paramteres of method)
# # data driven and parameterization can be done with return statements  in tuple format
#when you define fixture scope to class only it will run once before class is initiated and at the end





# import pytest
#
# #
# @pytest.fixture()
# #
# def setup():
#     print("i will be executing first")
#     yield
#     print("i will execute last")
#
# @pytest.mark.smoke
# def test_firstProgram():
#     print("hello")
#
# @pytest.mark.xfail
# def test_secondCreditCard():
#     print("good morning")
#
# #parameterization
# def test_CrossBrowser(crossBrowser):
#     print(crossBrowser)

# def test_CrossBrowser(crossBrowsers):
#     print(crossBrowsers)
#     print(crossBrowsers[2])