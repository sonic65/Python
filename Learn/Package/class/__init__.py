#构造函数 __init__()  | initial

class Student:

    def __init__(self,name,score):
        self.name = name
        self.score = score
    
    def print_score(self):  #实例方法必须要有self
        print("{0}分数{1}".format(self.name,self.score))

#self相当于C中的指针,JAVA|Node.JS中的this

s1 = Student("高宇航",100)
s1.print_score() #解释器的翻译为: Student.say_score(s1)
Student.print_score(s1)

'''
s1 = Student(self,"高宇航",100)这句话做了三件事
1. 创建对象 __new__() ,内存地址为(self) 
2. 初始化对象,构造函数 __init__()
3. 赋值 ("高宇航",100)给构造函数 name="",score=100
'''



'''
stack:
---------------
| id = 创建的对象地址(self) ---------------- 
| Type
| value:attr,method
| 
| 
|
---------------
'''

s1.salary = 10000  #新增实例属性
print(s1.salary)