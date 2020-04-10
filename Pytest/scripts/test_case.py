# -*- coding: utf-8 -*-
# __author__ = "maple"

import pytest
import allure
from uti.ExcelHandler import ExcelHandler
from uti.RequestHandler import RequestHandler
from uti.AllureHandler import AllureHandler
from uti.EmailHandler import EmailHandler
'''
1. 拿到Excel数据
2. 发请求
3. 生成测试用例报告
4. 发邮件
5. 断言

'''


class Test_case(object):
    @pytest.mark.parametrize('case', ExcelHandler().get_excel_data)
    def test_case(self, case):
        """  执行断言 """
        # print(case)
        # 发请求
        response = RequestHandler(case).get_response

        # 制作 allure 报告
        allure.dynamic.title(case['case_project'])
        allure.dynamic.description('<font color="red">请求URL：</font>{}<br />'
                                   '<font color="red">期望值：</font>{}'.format(case['url'], case['module']))
        allure.dynamic.feature(case['id'])
        allure.dynamic.story(case['method'])
        assert response[0] == response[1]

    def teardown_class(self):
        """  执行alllure命令 """

        AllureHandler().execute_command()
        # 发邮件
        EmailHandler().send_email()




