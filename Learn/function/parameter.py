#!/usr/bin/python3

def printme(str,*str1,**str2):
    print(str)
    print(str1) #加了星号 * 的参数会以元组(tuple)的形式导入
    print(str2) #加了两个星号 ** 的参数会以字典的形式导入。

    return
#printme()    #报错，必须要参数

printme("hello")  
printme("hello",2,3,4,a=2,b=3,c=5)
