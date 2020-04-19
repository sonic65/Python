#导入csv包
import csv

#with open()打开文件，既执行了打开文件，同时在方法结束后自动关闭文件，免去了我们忘记关闭文件的错误
with open("./Learn\DATA\dataCSV\data.csv","r",encoding="utf-8") as f:
    #读取csv文件
    values=csv.reader(f)
    print("打印产品信息、测试信息")
    for value in values:
        print(value[0], value[3])