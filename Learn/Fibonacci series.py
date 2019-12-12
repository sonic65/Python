#!/usr/bin/python3

# Fibonacci Series:斐波那契数列
# 两个数列的总和确定了下一个数

a, b = 0, 1
while b < 10:
    print(b)
    a,b = b, a+b  # b = a+b, a = b

#先运算右边,再赋值左边

i =256*256
print("i is :",i)

a,b = 0,1
while b < 1000:
    print(b,end=',') #关键字end可以用于将结果输出到同一行
    a,b = b,a+b