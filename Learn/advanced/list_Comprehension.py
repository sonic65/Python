#推导式（又称解析式）是Python的一种独有特性，
#推导式是可以从一个数据序列构建另一个新的数据序列的结构体。 
# 共有三种推导，在Python2和3中都有支持：
# 列表(list)推导式
# 字典(dict)推导式
# 集合(set)推导式

#partten
#variable = [out_exp for out_exp in input_list if out_exp == 2]

multiples = [i for i in range(30) if i %3 is 0]
print(multiples)

squared = []
for x in range(10):
    squared.append(x**2)

squared = [x**2 for x in range(10)]
print(squared)