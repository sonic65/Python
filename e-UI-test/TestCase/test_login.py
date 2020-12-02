#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import pytest
import allure
from tools.logger import log
from common.readconfig import ini
from page_object.loginpage import LoginPage

@allure.feature("测试bilibili登录")
class TestLogin:
    @pytest.fixture(scope='function', autouse=True)
    def open_bilibili_login(self, drivers):
        "打开B站登录页面"
        login = LoginPage(drivers)
        login.get_url(ini.url)
    
    @allure.story("登录操作")
    def test_001(self, drivers):
        "登录"
        login = LoginPage(drivers)
        login.input_username("淡い柠檬草")
        login.input_password("56749154b")
        login.click_login_button()
        result = re.search((r'哔哩哔哩', login.get_source))
        log.info()
        assert result

if __name__ == '__main__':
    pytest.main(['TestCase/test_login.py'])
