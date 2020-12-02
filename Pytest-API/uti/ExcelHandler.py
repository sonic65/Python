# -*- coding: utf-8 -*-
# __author__ = "maple"


'''

关于Excel表的操作
'''

import xlrd
import sys
sys.path.append("..")
from settings import conf

class ExcelHandler(object):

    @property
    def get_excel_data(self):
        # 获取到book对象
        book = xlrd.open_workbook(conf.TEST_CASE_PATH)
        # print(book)
        # 获取sheet对象
        sheet = book.sheet_by_index(0)
        # sheet = book.sheet_by_name('接口自动化用例')
        # sheets = book.sheets()  # 获取所有的sheet对象

        rows = sheet.nrows
        cols = sheet.ncols
        l = []
        # print(sheet.row_values(0))
        title = sheet.row_values(0)
        # 获取其他行
        for i in range(1, rows):
            # print(sheet.row_values(i))
        #将【title：列值】组装成字典
            l.append(dict(zip(title, sheet.row_values(i))))
            print(l)
        return l

if __name__ == '__main__':
    ExcelHandler().get_excel_data