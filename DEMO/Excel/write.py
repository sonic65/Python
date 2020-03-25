import xlwt

#设置表格样式
def set_style(name,height,bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style

#写Excel
def write_excel():
    path = '/Users/sonic/Project/Python/Learn/Excel/demo.xlsx'
    f = xlwt.Workbook() # 读的方法 xlwt.Workbook() 
    sheet1 = f.add_sheet('ASC',cell_overwrite_ok=True)
    row0 = ['url','method','message','code']
    colum0 = ['余书瑶','love','高宇航','/acs']

# write for Row0
    for i in range(0,len(row0)):
        sheet1.write(0,i,row0[i])
# write for colum0
    for i in range(0,len(colum0)):
        sheet1.write(i+1,0,colum0[i])

# write directly
    sheet1.write(3,3,'hello 书瑶') #在Row3 Colum3 写入‘hello python’
    sheet1.write(3,4,'hello 宇航') #在Row3 Colum3 写入‘hello python’
    sheet1.write(1,3,'2006/12/12') #在Row1 Colum3写入‘2006/12/12’
    # sheet1.write_merge(6,6,1,3,'未知') #合并行单元格 Row6 Colum1～3
    # sheet1.write_merge(1,2,3,3,'打游戏') #合并列单元格 Row1～2 Colum3
    f.save('test.xls')    

if __name__ == '__main__':
    write_excel()