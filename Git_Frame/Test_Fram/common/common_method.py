# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 11:53 上午
# @Author  :
# @Site    :
# @File    : common_method.py
import xlrd, json
from xlutils.copy import copy
import urllib
import urllib.request
import urllib.parse
import hashlib
import time,sys
import requests
from urllib.parse import quote
import string


#证书问题 # 禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

Consumer_Service_Id = 'ID1'
Provider_Domain_Id = 'ID2'
md5_key = 'md5_key'
url_ = 'https://baidu.com'

class commonMethod():

    # 读取excle文件转换成json列表
    # 参数path，是excle文件存放路径
    def read_excle(self, path):
        final_list = []
        rb = xlrd.open_workbook(path)  # 打开文件
        # print(wb.sheet_names())#获取所有表格名字
        sheet1 = rb.sheet_by_index(0)  # 通过索引获取表格 tab
        wb = copy(rb)
        wbsheet1 = wb.get_sheet(0)
        ncols = sheet1.ncols  #列
        nrows = sheet1.nrows  #行
        #把excle转换成jaon列表
        for i in range(1, nrows):
            object_json = {'rowIndex':i}
            for a in range(ncols):
                object_json[sheet1.row_values(0)[a]] = sheet1.row_values(i)[a]
            final_list.append(object_json)
        return final_list

    #写excle##
    # 参数 path 文件存放路径
    #  row 行
    # col 列
    # message 录入的信息
    def write_excle(self, path, row, col, meassage):
        rb = xlrd.open_workbook(path)  # 打开文件
        wb = copy(rb)
        wbsheet1 = wb.get_sheet(0)
        wbsheet1.write(row, col, meassage)
        wb.save(path)

    #获取某个接口返回的结果
    # 此方法可以用来进行接口串联测试，来获取之前接口返回的值
    # 参数 path: excle路径
    # 参数 url:请求地址
    def get_url_response(self,path,url):
        read_excle_result = self.read_excle(path)
        for result in read_excle_result:
            if result['url'] == url:
                this_url_response = result['code']
                return this_url_response

    def token_md5(self):
        t = time.time()
        timeStamp = (round(t * 1000))
        signStr = 'ID1' + "-" + 'ID2' + "-" + str(
            timeStamp) + "-" + 'md5key'
        m1 = hashlib.md5()
        # 使用md5对象里的update方法md5转换
        m1.update(signStr.encode("utf-8"))
        signVal = m1.hexdigest()
        # print(timeStamp, signVal)
        return signVal, str(timeStamp)            

    #请求函数
    # 参数 url:请求地址
    # 参数 data: 请求参数
    # 参数 method: 请求方法 post,get等
    # 参数 headers: 请求头
    def http_special_query(self,url, data, method, headers):
        if headers is None or str(headers).upper() == 'NONE' or headers == '':
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        #python3处理含有中文的url  url=quote(url, safe=string.printable)
        put_request = urllib.request.Request(url=quote(url, safe=string.printable), data=data.encode('utf-8'), headers=headers, method=method) #发起请求
        res = urllib.request.urlopen(put_request) #返回参数
        result = res.read().decode('utf-8') #请求返回的body
        return result

if __name__ == '__main__':
    test_data_list = commonMethod().read_excle(r'../testdata/reg.xls')
    for test_data in test_data_list:
        excleRow = test_data['rowIndex']
        url = url_ + test_data['url']
        sigRes = commonMethod().token_md5()
        headers = {
                    'Consumer_Service_Id': Consumer_Service_Id,
                    'Provider_Domain_Id': Provider_Domain_Id,
                    'Sig':sigRes[0],
                    'Time_Stamp':sigRes[1]
        }
        # print(url,test_data['params.py'],test_data['method'],headers)
        res = commonMethod().http_special_query(url, test_data['params.py'], test_data['method']
                                                ,headers)  ###发起请求
        print(type(res),res)
        res_to_json = json.loads(res)  ####返回的json结果转dict
        print(res_to_json)
        commonMethod().write_excle(r'../testdata/reg.xls', excleRow, 4, res_to_json['code'])  ###写入结果到excle

        jsonPathList = test_data['result_key'].split('.')  ####需要获取的返回结果，json的路径
        for jsonPath in jsonPathList:
            if isinstance(res_to_json, list) and (jsonPath.isdigit() == False):  # 判断路径为非数字，取list中的第一个元素
                res_to_json = res_to_json[0]
            elif jsonPath.isdigit():  # 如果路径中包含了下标，取对应下标的值
                res_to_json = res_to_json[int(jsonPath)]
            else:  # 正常路径的值
                res_to_json = res_to_json[jsonPath]
        issuccess = '失败'
        if res_to_json == test_data['code']:  # 如果断言成功，写入结果到excle
            issuccess = '成功'
        commonMethod().write_excle(r'../testdata/reg.xls', excleRow, 7, issuccess)

