#!usr/bin/python
# -*- coding: UTF-8 -*-

conter = 100 # 赋值整型变量
miles = 100.22 # 浮点型变量
name = "John" # 字符串

print conter
print miles
print name

a = b = c = 1

print a,b,c


a,b,c = 1,100.22,"John"
print a,b,c

"""
Python有五个标准的数据类型：
Numbers（数字）{int,long,float,complex}
String（字符串）
List（列表）
Tuple（元组）
Dictionary（字典）
"""

#String
str = "Hello World!"

print str[1]
print str[1:5]
print str*2
print str + "Test"
print str[1:2:5]

#List
list = ['runoob',786,2.23,'john',70.2]

print list
print list[0]
print list[1:4]
print list*2
print list[3:]

#Tuple 元组 不能二次赋值 类似list
tuple = ('runoob',786,2.23,'Jimmy',70.2)

print tuple

#Dictionary 字典用"{ }"标识。字典由索引(key):它对应的值value组成。 key:value
dict = {}
dict['one'] = 'This is one'
dict[2] = "This is two"
tinydict = {'name':'Michael','code':'8848','dept':'tech'}

print dict['one']
print dict[2]
print tinydict
print tinydict.keys()
print tinydict.values()

#数据类型转换 将数据类型作为函数名即可
x = 10
float(x)
x = 10.1
print(x)