# -*- coding: utf-8 -*-
# __author__ = "maple"


'''

关于Excel表的操作
'''

import xlrd
import conf
from xlutils.copy import copy


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
            l.append(dict(zip(title, sheet.row_values(i))))
        return l

    # message 录入的信息
    def write_excle_result(self, path, row, col, meassage):
        rb = xlrd.open_workbook(path)  # 打开文件
        wb = copy(rb)
        wbsheet = wb.get_sheet(0)
        wbsheet.write(row, col, meassage)
        wb.save(conf.TEST_CASE_PATH)

    def get_test_data(self, data_list, case_name):
        pass

if __name__ == '__main__':
    ExcelHandler().get_excel_data