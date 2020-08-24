#题目：两个变量值互换

def exchange(a,b):
    a,b = b,a
    print(a,b)
    return(a,b)


x = 10
y = 20
exchange(x, y)
# print(x, y )