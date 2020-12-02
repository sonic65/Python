# -*- coding: utf-8 -*-
# @Time    : 2020/12/01 11:53 上午
# @Author  : sonic
# @Site    :
# @File    : excelHandler.py
# @comment : Excel operation

import xlrd
from xlutils.copy import copy

path = r'../testData/reg.xls'


class excelHandler():
    
    # 读取Excel
    def read_excel(self, path):
        data_list = []
        rb = xlrd.open_workbook(path)
        sheet1 = rb.sheet_by_index(0)
        wb = copy(rb)
        wbsheet1 = wb.get_sheet(0)
        ncols = sheet1.ncols 
        nrows = sheet1.nrows

        #把Excel转化成json列表
        for i in range(1, nrows):
            json_object = {'rowIndex', i}
            for a in range(ncols):
                json_object[sheet1.row_values(0)[a]] = sheet1.row_values(i)[a]
            data_list.append(json_object)
            # print(json_object) 
        return data_list


    # 写入Excel
    def write_excel():
        wb = xlrd.open_workbook(path)


if __name__ == "__main__":
    excelHandler().read_excel(path)