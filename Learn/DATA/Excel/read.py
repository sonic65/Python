import xlrd
from datetime import date,datetime

file = 'test.xls'

def read_excel():

    wb = xlrd.open_workbook(filename=file)
    print('All sheet name:',wb.sheet_names())

    sheet1 = wb.sheet_by_index(0) #通过索引获取表格
    sheet2 = wb.sheet_by_name('ASC') #通过名字获取表格
    print('sheet code',sheet1,sheet2)
    print('sheet content:',sheet1.name,sheet1.nrows,sheet1.ncols)

    rows = sheet1.row_values(2) #Get Row2
    clos = sheet1.col_values(3) #Get colum3
    # print('sheet1 row[2]',rows)
    # print('sheet1 colum[3]',clos)
    # #获取单元格内容 
    # print(sheet1.cell(1,0).value)  
    # print(sheet1.cell_value(1,0))
    # print(sheet1.row(1)[0].value)
    # #获取单元格类型
    # print(sheet1.cell(2,0).ctype)
    print('sheet1 row[0]')



if __name__ == '__main__':
    read_excel()
