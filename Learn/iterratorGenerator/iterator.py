#迭代器有两个基本的方法：iter() 和 next()。
import sys

list=[1,2,3,5]
it = iter(list)

'''
for x in it:
    print(x)
'''

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()    