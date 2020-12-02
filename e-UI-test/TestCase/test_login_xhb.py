#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import pytest
import allure
from tools.logger import log
from common.readconfig import ini
from page_object.login_page import LoginPage

@allure.feature("测试xht登录")
class TestLogin:
    @pytest.fixture(scope='function', autouse=True)
    def open_xht_login(self, drivers):
        "打开xkt登录页面"
        login = LoginPage(drivers)
        login.get_url(ini.url)
    
    @allure.story("登录操作")
    def test_001(self, drivers):
        "登录"
        login = LoginPage(drivers)
        login.input_username("13166229623")
        login.input_password("56749154aA")
        login.click_login_button()
        result = re.search((r'晓黑板', login.get_source))
        log.info()
        assert result

if __name__ == '__main__':
    pytest.main(['TestCase/test_login_xhb.py'])
