import csv

filename='/Users/gaoyuhang/Project/Python/work/list.csv'


arr = []
for line in open(filename):
    for x in line.split(' '):
      arr.append(x)
print("\n".join(arr))


with open(filename) as file:
 lines = file.readlines()#读取每一行
 
a = ''#空字符（中间不加空格）
for line in lines:
 a += line.strip()#strip()是去掉每行末尾的换行符\n 1
c = a.split()#将a分割成每个字符串 2
b = ''.join(c)#将c的每个字符不以任何符号直接连接 3
print(a)
print(b)
#打印a,b观察不同