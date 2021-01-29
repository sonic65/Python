import xlrd
import json
import requests
from bs4 import BeautifulSoup

import xlrd

# row 是行
# col 是列

file_path = r'../data/Test_Case.xls'

# 拿到book对象 xlrd.open_workbook方法
book = xlrd.open_workbook(file_path)
print(book)
# 拿到表格中对象 按索引获取
sheet = book.sheet_by_index(0)
print(sheet)

# 行,列 获取到所有的行和列 sheet.nrows方法, sheet.ncols方法
rows, cols = sheet.nrows, sheet.ncols
print(rows, cols)

# for循环出每一行
for row in range(rows):
    print(sheet.row_values(row))
#
# # for循环出每一列
# for col in range(cols):
#     print(sheet.col_values(col))
