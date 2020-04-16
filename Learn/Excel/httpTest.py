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

class HttpTest():
    # 读excel
    def auto_test_excel(self):
            # 
        url0 = 'http://localhost:8886/'
        path = r'/Users/sonic/Project/Python/Pytest/Data/Test_Case.xlsx'
        rb = xlrd.open_workbook(path)  # 打开文件
        sheet1 = rb.sheet_by_index(0)  # 通过索引获取表格
        print(rb)
        ncols = sheet1.ncols
        nrows = sheet1.nrows
        # print(rb.sheet_names())#获取所有表格名字

# table.row_values(rowx, start_colx=0, end_colx=None)   #返回由该行中所有单元格的数据组成的列表
        # print(sheet1.row_values(1,3,6))

#两种循环方式

        list = [] #把数据以字典形式存在字符串中。一个字段


        # for i in range(0, nrows):
        #     print(sheet1.row_values(i)) #所有行
        #     print(sheet1.row_values(i, 3)) #Row3之后的所有行
        #     print(sheet1.row_values(i, 2)[1]) #Row3 + 1行
        #     print(list)

        for row in range(1, nrows):
            # print(sheet1.row_values(row)) #所有行
            # print(sheet1.row_values(row, 3)) #Row3之后的所有行
            # print(sheet1.row_values(row, 2)[1]) #Row3 + 1行
            # print(sheet1.row_values(row, 2)[0]) #Row3 
            print(sheet1.row_values(row, 2, 3)[0])
                
if __name__ == '__main__':

    HttpTest().auto_test_excel()
