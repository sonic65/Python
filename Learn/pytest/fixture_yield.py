from selenium import webdriver
import pytest

# TearDown
@allure.feature('Testing') # @allure.feature # 用于定义被测试的功能，被测产品的需求点
## yield
@pytest.fixture()
def open_url_fixture_yield():
        print("Before Test")
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        yield
        print("After Test")
        driver.quit()

def test_001(open_url_fixture_yield):
        print("test001")    

def test_002(open_url_fixture_yield):
        print("test002")


# 结果 
'''
fixture_yield.py 
Before Test
test001
.After Test
Before Test
test002
.After Test
'''

# ##addfinalizer
# @pytest.fixture()
# def open_url_fixture_addfinalizer(request):
#         print("Before Test")
#         driver = webdriver.Chrome()
#         driver.get("http://bing.com")

#         def finalizer():
#                 driver.quit()
        
#         print("After Test")
#         request.addfinalizer(finalizer)

# def test_001(open_url_fixture_addfinalizer):
#         print("test003")

# def test_002(open_url_fixture_addfinalizer):
#         print("test004")