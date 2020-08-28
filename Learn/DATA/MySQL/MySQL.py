#!/usr/bin/python

import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",       # 数据库主机地址
  user="us",    # 数据库用户名
  passwd="pw",   # 数据库密码
  database="db"      #DB名
)

mycursor = mydb.cursor()

print(mydb)

sql = "show tables"
 
mycursor.execute(sql)
 
myresult = mycursor.fetchall()     # fetchall() 获取所有记录
 
for x in myresult: print(x)
 
