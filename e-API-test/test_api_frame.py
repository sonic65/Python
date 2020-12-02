#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os, json
import pytest
import allure
from common.common_method import *
import requests

url_ = 'https://janus'
# url_ = ''

#证书问题 # 禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# #回归测试#
filepath = r'./testdata/reg.xls'

class TestDemo():
    @allure.severity("minor") #  报告中展示的优先级
    @allure.feature("接口测试") # 报告中展示的一级标签
    @allure.story('Test')    # 报告中展示的二级标签
    @pytest.mark.parametrize( # 定义的参数变量，可以赋值后在test函数里面使用
        "test_data",# 定义变量 test_data, 在测试函数使用
         commonMethod().read_excle(filepath))# 读取取到的excle里面的参数，并赋值给 test_data
    # @pytest.mark.flaky(reruns=2) # 执行测试失败的重试次数，目前设置的为2次重试

    def test(self, test_data): 
        '''翰林院接口自动化测试----Test''' #这个文本会在报告头展示
        try:
            excleRow = test_data['rowIndex'] ###当前读取的excle行
            ###请求头
            #报告中用来记录测试步骤
            with allure.step('开始发起请求：'+"{0}: {1}".format(str(test_data['method']), test_data['url'])): 
                url = url_ + test_data['url']
                url = test_data['url']
                headers = None
                res = commonMethod().http_special_query(url,test_data['params'],test_data['method'],headers) ###发起请求                
                with allure.step('返回消息'+str(res)): ###在allure报告中展示返回消息
                    allure.attach('返回消息', str(res), allure.attachment_type.TEXT) ###在allure报告中展示添加为TEXT附件，支持多种附件，需要更改比如png allure.attachment_type.PNG
                res_to_json = json.loads(res) ####返回的结果转json               
                commonMethod().write_excle(filepath,excleRow,7,res_to_json['code']) ###写入结果到excle
                # commonMethod().write_excle(filepath,excleRow,8,res_to_json['success']) ###写入结果到excle             
                jsonPathList = test_data['result_key'].split('.') ####需要获取的返回结果，json的路径      
                for jsonPath in jsonPathList:
                    if isinstance(res_to_json, list) and (jsonPath.isdigit() == False): #判断路径为非数字，取list中的第一个元素
                        res_to_json = res_to_json[0]
                    elif jsonPath.isdigit(): #如果路径中包含了下标，取对应下标的值
                        res_to_json = res_to_json[int(jsonPath)]
                    else: #正常路径的值
                        res_to_json = res_to_json[jsonPath]
                issuccess = '失败'            
                if res_to_json == test_data['except']: #如果断言成功，写入结果到excle
                    issuccess = '成功'
                commonMethod().write_excle(filepath, excleRow, 9, issuccess)
                assert res_to_json == test_data['except']###断言，用来判断当前测试是否通过
       
        except Exception as e:
            pytest.fail("测试失败退出！")####测试失败
            pytest.xfail(str(e)) #####异常导致测试失败，输出异常信息

if __name__ == '__main__':
    os.system('pytest -s ./test_frame.py::TestDemo::test_ --alluredir report/result') #执行pytest测试类，并输出allure格式数据到 report文件夹
    os.system('allure generate report/result -o report/allure_html --clean') #html报告生成