from selenium import webdriver
import pytest

# TearDown

'''
##addfinalizer
@pytest.fixture()
def open_url_fixture_addfinalizer(request):
        print("Before Test")
        driver = webdriver.Chrome()
        driver.get("http://bing.com")

        def finalizer():
                driver.quit()
                print("After Test")

        request.addfinalizer(finalizer)

def test_003(open_url_fixture_addfinalizer):
    print("test003")

def test_004(open_url_fixture_addfinalizer):
    print("test004")

'''

#结果
'''
fixture_addfinalizer.py 
Before Test
test003
.After Test
Before Test
test004
.After Test
'''

##多个addfinalizer 

@pytest.fixture()
def open_url_fixture_addfinalizer(request):
        print("Before Test")
        driver = webdriver.Chrome()
        driver.get("http://bing.com")

        def finalizer():
                driver.quit()
                print("After Test")

        def finalizer2():
                print("After Test2")

        request.addfinalizer(finalizer)
        request.addfinalizer(finalizer2)

def test_003(open_url_fixture_addfinalizer):
    print("test003")

def test_004(open_url_fixture_addfinalizer):
    print("test004")
