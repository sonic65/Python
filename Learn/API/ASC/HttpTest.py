#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'wx'

import requests
import json
import argparse
import xlwt
import xlrd
import unittest
import hashlib
import time
import datetime
import sys
from xlutils.copy import copy


class HttpTest():
    # 读excel
    def auto_test_excel(self):
        try:
            # 
            url0 = 'http://localhost:8886/'
            path = '/Users/sonic/Project/Python/Pytest/data/Test_Case.xls'
            print(self.sign_md5())
            sigRes = self.sign_md5()
            header = {"User-Agent": "Chrome/51.0.2704.103"}

            rb = xlrd.open_workbook(path)  # 打开文件
            # print(wb.sheet_names())#获取所有表格名字
            sheet1 = rb.sheet_by_index(0)  # 通过索引获取表格
            wb = copy(rb)
            wbsheet1 = wb.get_sheet(0)
            ncols = sheet1.ncols
            nrows = sheet1.nrows

            for row in range(1, nrows):
                print('----------------------------------当前执行--------第',row,'行----------------------------------')
                res = None
                url = sheet1.row_values(row, 2, 4)[0]
                method = sheet1.row_values(row, 4, 5)[0]
                params = sheet1.row_values(row, 5, 6)[0]
                if (method == 'GET'):
                    if (params == None or params == ''):
                        # 前面已经通过 copy 方法获取了writeOpenXlsx
                        # 通过get_sheet()获取的sheet有write()方法
                        res = self.get_invoke(url,params,header)
                    else:
                        res = self.get_invoke(url+'?'+params,None,header)
                else:
                    data_json = None
                    header['Content-Type']='application/json'
                    if(params != None and params != '' and len(params) !=0):
                        data_json = json.dumps(json.loads(params))
                    res = self.post_invoke(url, data_json, header)

                #返回所有结果    
                # print('执行结果返回:',str(res))  
                #返回code和message   
                code = res['code']
                msg = res['message']
                # print('测试接口：',url,'\n测试结果：code：',code,",“message：",msg)       
                print('测试接口：',url,'\n测试结果：',res)                     

                if(res != None):
                    code = res['code']
                    msg = res['message']
                    wbsheet1.write(row, 9, code)
                    wbsheet1.write(row, 10, str(msg))
                    res=None
                    data_json=None
            wb.save(path)
        except BaseException as e:
            print("Unexpected error:", sys.exc_info()[0],sys.exc_info())
            print('发生异常')
        else:
            print('未发生异常')

    #执行调用
    #1、不管json是str还是dict，如果不指定headers中的content-type，默认为application/json
    #2、data为dict时，如果不指定content-type，默认为application/x-www-form-urlencoded，相当于普通form表单提交的形式
    #3、data为str时，如果不指定content-type，默认为application/json
    #4、用data参数提交数据时，request.body的内容则为a=1&b=2的这种形式，用json参数提交数据时，request.body的内容则为'{"a": 1, "b": 2}'的这种形式
    def post_invoke(self,url,data,headers=None):
        res = None
        if headers ==None:
            res = requests.post(url=url,data=data)
        else:
            res = requests.post(url=url,data=data,headers=headers)
        return json.loads(res.content.decode())

    def get_invoke(self,url,data,headers=None):
        res = None
        if headers == None:
            res = requests.get(url=url,data=data)
        else:
            res = requests.get(url=url,data=data,headers=headers)
        return  json.loads(res.content.decode())

    def sign_md5(self):
        t = time.time()
        timeStamp = (round(t * 1000))
        signStr = '3825720472286642210' + "-" + '1515795216911630337' + "-" + str(
            timeStamp) + "-" + 'ee54bcd1-662c-47ae-8117-76946e3d4e1f'
        m1 = hashlib.md5()
        # 使用md5对象里的update方法md5转换
        m1.update(signStr.encode("utf-8"))
        signVal = m1.hexdigest()
        return signVal,str(timeStamp)


if __name__ == '__main__':
    # ss = '{"status":0,"providerId":"1515795216911630337","actionUrl":"employees.page"\n}'
    # ss = ss.replace('\n','').replace("\"","'")
    # print(ss)


    # parser = argparse.ArgumentParser(description='manual to this script')
    # parser.add_argument('--params.py', type=str, default=None)
    # args = parser.parse_args()
    # print("测试参数传递",args.params.py)
    httpDemo = HttpTest()
    httpDemo.auto_test_excel()
    # header = {
    #     "Consumer_Service_Id":"3282200401156294249"
    # }
    # res = httpDemo.get_invoke("http://localhost:8886/employees/es/",None,header)
    # print("返回数据:",res)


