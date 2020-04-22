import xlrd
import json
import requests
from bs4 import BeautifulSoup

import xlrd

# row 是行
# col 是列

file_path = r'../data/Test_Case.xlsx'

# 拿到book对象 xlrd.open_workbook方法
book = xlrd.open_workbook(file_path)
print(book)

# 拿到表格中对象 按索引获取
sheet = book.sheet_by_index(0)
print(sheet)

# 按名字获取
sheet1 = book.sheet_by_name('login')
print(sheet1)

# 行,列 获取到所有的行和列 sheet.nrows方法, sheet.ncols方法
rows, cols = sheet.nrows, sheet.ncols
print(rows, cols)

# for循环出每一行
for row in range(rows):
    print(sheet.row_values(row))

# for循环出每一列
for col in range(cols):
    print(sheet.col_values(col))

# 按索引取出行列
print(sheet.row_values(2))

print(sheet.col_values(0))

print(sheet.cell(0, 0))

# 将行和列的值拼接在一起 组合成[{},{}]的样式 zip拉在一起 dict转一下
l = []
title = sheet.row_values(0)
for i in range(1, rows):
    l.append(dict(zip(title, sheet.row_values(i))))

print(l)


def get_excel_data():
    file_path = r'../data/Test_Case.xlsx'

    # 获取到book对象
    book = xlrd.open_workbook(file_path)
    # print(book)
    # 获取sheet对象
    sheet = book.sheet_by_index(0)
    # sheet = book.sheet_by_name('接口自动化用例')
    # sheets = book.sheets()  # 获取所有的sheet对象

    rows, cols = sheet.nrows, sheet.ncols
    l = []
    # print(sheet.row_values(0))
    title = sheet.row_values(0)
    # print(title)
    # 获取其他行
    for i in range(1, rows):
        # print(sheet.row_values(i))
        l.append(dict(zip(title, sheet.row_values(i))))

    return l
r = requests.get('https://www.cnblogs.com/Neeo/articles/11667962.html')
s = BeautifulSoup(r.text, 'html.parser')
print(s.find('title').text)

