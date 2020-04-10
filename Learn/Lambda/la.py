foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
sl = [1,2,3,1]


from functools import reduce


new_foo = filter(lambda x: x % 3 == 0, foo)  #对于序列中的元素进行筛选，最终获取符合条件的序列
new_sl = map(lambda a,b:a+b,sl,foo)  #map()遍历序列，对序列中每个元素进行操作，最终获取新的序列。
new_fl = reduce(lambda a,b:a+b,sl)  #reduce() 对于序列内所有元素进行累计操作

print(list(new_foo))
print(list(new_sl))
print(new_fl)