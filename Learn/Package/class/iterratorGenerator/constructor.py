#  __iter__() 与 __next__() 
# 面向对象 https://www.runoob.com/python3/python3-class.html

class MyNumbers:
    def __iter__(self):
        self.a = 1 
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myClass = MyNumbers()
myIter = iter(myClass)

print(next(myIter))
print(next(myIter))
print(next(myClass))
print(next(myClass))