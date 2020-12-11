#assert expression

#if not expression:
#    raise AssertionError

import pytest
import allure

@allure.feature("测试")
def test_001():
    x = 1
    if x == 1:
        print(x)
    assert x==1

@allure.feature("==")
def test_002():
    ss = str("Hello World")
    xx = str("Hello")
    assert xx in ss

if __name__ == '__main__':
    pytest.main(['-s', '-q',  '--alluredir', './result/'])
