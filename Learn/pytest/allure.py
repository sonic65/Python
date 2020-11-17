import pytest
import allure


@allure.feature('Testing') # @allure.feature # 用于定义被测试的功能，被测产品的需求点

class TestSample(object):

    def setup_class(self):
        self.a = 'aaaaa'
        print("------ setup before class UserLogin ------")

    @allure.story('001') #@allure.story # 用于定义被测功能的用户场景，即子功能点
    def test_sample_1(self):
        allure.attach('杨婷婷') #allure.attach # 用于向测试报告中输入一些附加的信息，通常是一些测试数据信息

        assert 'hello' in 'hello world'

    @allure.story('002') #@allure.story
    def test_sample_2(self):
        assert 'OK' in 'are you ok?'


if __name__ == '__main__':
    import os

    pytest.main(['-s', '-q', 'test_sample.py', '--alluredir', './result/'])
    os.system('allure serve ./result/')