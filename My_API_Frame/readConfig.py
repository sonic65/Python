import os
import configparser
import getpathInfo

path = getpathInfo.get_Path() #调用实例化
config_path = os.path.join(path,'common','config.ini') #这句话是在path路径下再加一级
config = configparser.ConfigParser() #调用外部的读取配置文件的方法
config.read(config_path,encoding='utf-8')

class ReadConfig():
    def get_http(self,name):
        value = config.get('HTTP',name)
        return value

    def get_email(self,name):
        value = config.get('EMAIL',name)
        return value

    def get_mysql(self,name):
        value = config.get('DATABASE',name)
        return value       

    def get_Url(self,name):
        scheme = config.get('HTTP','scheme') 
        url0 = config.get('HTTP','baseurl') 
        url = scheme + '://' + url0  + ':8888' + '/login' + '?'
        return url

 
if __name__ == '__main__':# 执行该文件，测试下是否OK
    print('HTTP BaseURL:', ReadConfig().get_http('baidu'))
    print('Email ON_OFF:', ReadConfig().get_email('app'))
    print('DATABSE:'     , ReadConfig().get_mysql('learning'))
    print('URL:'     , ReadConfig().get_Url(''))
