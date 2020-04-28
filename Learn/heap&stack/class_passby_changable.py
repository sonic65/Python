#可变对象。
#定义b，

b = [10,20]
print('b',id(b))
print(b)

def f2(m):
    print('b',id(m))
    print('b',id(b))
    m.append(30)

f2(b)
print('b',id(b))
print(b)

