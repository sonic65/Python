import allure
import pytest

@allure.feature('TestModule01')
@allure.story('TestStory01')
@allure.severity('blocker')
@allure.issue("http://www.baidu.com")
@allure.testcase("http://www.testlink.com")
def test_case01():
    '''
    discription1
    '''
    assert 'hello' in 'hello world'

@allure.feature('TestModule01')
@allure.story('TestStory01')
@allure.severity('critical')
def test_case02():
    '''
    discription2
    '''
    assert '你好' in 'hello world'

@allure.feature('TestModule02')
@allure.story('TestStory01')
@allure.severity('Trivial')
def test_case03():
    '''
    discriptionAAA
    '''
    assert 5<6

@allure.step('str add')
def str_add(str1, str2):
    if not isinstance(str1, str):
        return "%s is not a string" % str1
    if not isinstance(str2, str):
        return "%s is not a string" % str2
    return str1 + str2

@allure.feature('TestModule02')
@allure.story('TestStory01')
@allure.severity('Normal')
@allure.description('测试报告')
@allure.title('测试标题')
def test_case04():
    '''
    discription3
    '''
    str1 = 'hello'
    str2 = 'world'
    assert str_add(str1,str2) == 'helloworld'

if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])
