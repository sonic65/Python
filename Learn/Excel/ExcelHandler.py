# -*- coding: utf-8 -*-
# __author__ = "maple"


'''

关于Excel表的操作
'''

import xlrd


class ExcelHandler(object):

    @property
    def get_excel_data(self):
        # 获取到book对象
        book = xlrd.open_workbook('Test_Case.xlsx')
        # print('book:',book)
        # 获取sheet对象
        sheet = book.sheet_by_index(0)
        # sheet = book.sheet_by_name('login')
        sheets = book.sheets()  # 获取所有的sheet对象

        rows, cols = sheet.nrows, sheet.ncols
        l = []
        # print('sheet.row_values:',sheet.row_values(0))
        title = sheet.row_values(0)
        # 获取其他行
        for i in range(1, rows):
            # print(sheet.row_values(i))
            l.append(dict(zip(title, sheet.row_values(i))))
        print('list:',l)
        return l

if __name__ == '__main__':
    ExcelHandler().get_excel_data()