f = open("E:\Work\Project\Python\Learn\DATA\dataTXT\data.txt","a")
f.write("xxxxxxx\nxxxx\n")
f.close()

"""
open的第一个参数是文件名。第二个(mode 打开模式)决定了这个文件如何被打开。
如果你想读取文件，传入r
如果你想读取并写入文件，传入r+
如果你想覆盖写入文件，传入w
如果你想在文件末尾附加内容，传入a
"""