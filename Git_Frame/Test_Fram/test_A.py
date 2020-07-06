#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'wx'
__update__ = 'yh'

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

#证书问题 # 禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#全局变量
Consumer_Service_Id = 'yuhang'
Provider_Domain_Id = 'yuhang'
md5_key = 'aayu'
url_daily = 'http://baidu.com'
url_prod = 'http://baidu.com'
file_path = '/Users/sonic/Project/Python/API/test.xls'


class HttpTest():
    # 读excel
    def auto_test_excel(self):

        url0 = url_daily
        path = file_path
        sigRes = self.sign_md5()
        header = {

            'Consumer_Service_Id': Consumer_Service_Id,
            'Provider_Domain_Id': Provider_Domain_Id,
            'Sig':sigRes[0],
            'Time_Stamp':sigRes[1]
        }
        rb = xlrd.open_workbook(path)  # 打开文件
        # print(wb.sheet_names())#获取所有表格名字
        sheet1 = rb.sheet_by_index(0)  # 通过索引获取表格
        wb = copy(rb)
        wbsheet1 = wb.get_sheet(0)
        ncols = sheet1.ncols
        nrows = sheet1.nrows
        # print(header)

        for row in range(1, nrows):
            print('----------------------------------当前执行--------第',row,'行----------------------------------')
            res = None
            url = url0+sheet1.row_values(row, 0, 1)[0]
            method = sheet1.row_values(row, 1, 2)[0]
            params = sheet1.row_values(row, 2, 3)[0]
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
                wbsheet1.write(row, 3, code)
                wbsheet1.write(row, 4, msg)
                res=None
                data_json=None
        wb.save(path)
        
    #执行调用
    #1、不管json是str还是dict，如果不指定headers中的content-type，默认为application/json
    #2、data为dict时，如果不指定content-type，默认为application/x-www-form-urlencoded，相当于普通form表单提交的形式
    #3、data为str时，如果不指定content-type，默认为application/json
    #4、用data参数提交数据时，request.body的内容则为a=1&b=2的这种形式，用json参数提交数据时，request.body的内容则为'{"a": 1, "b": 2}'的这种形式
    def post_invoke(self,url,data,headers=None):
        res = None
        if headers ==None:
            res = requests.post(url=url,data=data,verify=False)
        else:
            res = requests.post(url=url,data=data,headers=headers,verify=False)
        return json.loads(res.content.decode())

    def get_invoke(self,url,data,headers=None):
        # print(url)
        # print(Data)
        # print(headers)
        res = None
        if headers == None:
            res = requests.get(url=url,data=data,verify=False)
        else:
            res = requests.get(url=url,data=data,headers=headers,verify=False)
        return  json.loads(res.content.decode())

    def sign_md5(self):
        t = time.time()
        timeStamp = (round(t * 1000))
      
        #UAT 服务id，domainId，key  
        signStr = Consumer_Service_Id + "-" +  Provider_Domain_Id  + "-" + str(
            timeStamp) + "-" + md5_key
        m1 = hashlib.md5()
        # 使用md5对象里的update方法md5转换
        m1.update(signStr.encode("utf-8"))
        signVal = m1.hexdigest()
        return signVal,str(timeStamp)


if __name__ == '__main__':
    # #执行测试
    print('Header：',HttpTest().sign_md5())
    httpDemo = HttpTest()
    httpDemo.auto_test_excel()