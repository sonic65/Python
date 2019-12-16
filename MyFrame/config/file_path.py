import os


print("当前目录",os.path.abspath(".")) #当前目录
file_path = os.path.dirname(os.path.abspath(".")) #OS Path的上一级
config_path = file_path + '\config\config.ini'  #OS Path的上一级+confi + config.ini
print("filepath" + file_path)
print("CONFIG",config_path)


