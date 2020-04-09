import os
import getpathInfo# 自己定义的内部类，该类返回项目的绝对路径
#调用读Excel的第三方库xlrd
import xlrd
import xlwt

# 拿到该项目所在的绝对路径
path = getpathInfo.get_Path()

class ReadExcel():
    def get_xls(self,xls_name,sheet_name):


        #xls路径  = path + filename
        xlsPath = os.path.join(path,'testFile','case',xls_name)
        #打开用例
        rb = xlrd.open_workbook(xlsPath)
        #获取sheet
        sheet1 = rb.sheet_by_name(sheet_name)

        # wb = xlrd.open_workbook(xlsPath)
        print(xlsPath)
        print(wb.sheet_names())

        ncols = sheet1.ncols
        nrows = sheet1.nrows

        for row in range(1, nrows):
            print('----------------------------------当前执行--------第',row,'行----------------------------------')
            res = None
            url = url0+sheet1.row_values(row, 0, 1)[0]
            method = sheet1.row_values(row, 1, 2)[0]
            params = sheet1.row_values(row, 2, 3)[0]


if __name__ == '__main__':#我们执行该文件测试一下是否可以正确获取Excel中的值
    print(ReadExcel().get_xls('userCase.xlsx', 'login'))
    print(ReadExcel().get_xls('userCase.xlsx', 'login')[0][1])