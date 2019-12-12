#!/usr/bin/python3

'''
def 函数名（参数列表）：
    函数体
'''

def hello():
    print("Hello Python") 


hello()
hello()

def area (width,height):
    return width * height

def print_welcome(name):
    print("Welcome",name)

print_welcome("Runoob")
w = 4
h = 5
print(area(w,h))
print("width = ",w, "height = ", h, "area =", area(w,h))
