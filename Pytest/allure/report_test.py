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
    discription3
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
def test_case04():
    '''
    discription3
    '''
    str1 = 'hello'
    str2 = 'world'
    assert str_add(str1,str2) == 'helloworld'

if __name__ == '__main__':
    file = open('../report.html','rb').read()
    allure.attach('test_report', file, allure.attach_type.HTML)

    '''
在报告中增加附件：allure.attach(’arg1’,’arg2’,’arg3’)：
arg1：是在报告中显示的附件名称
arg2：表示添加附件的内容
arg3：表示添加的类型(支持:HTML,JPG,PNG,JSON,OTHER,TEXTXML)
    '''

    pytest.main(['-s', '-q', '--alluredir', './report/xml'])
