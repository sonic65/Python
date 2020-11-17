class Neko(object): #neko对象
    sex = "girl"  #neko的常量
    def __init__(self,neko_name): #neko的函数
        self.name = neko_name #赋值给neko_name
        print("hello")

    def c(self,c_name):  #neko的函数2
        self.name=c_name
        print("name ="+ c_name)    

    def n(self,neko_name):
        self.name=neko_name    

th8 = Neko("reimu") 
#一个neko的实例 ("reimu")赋值给neko_name 初始化会执行__init__函数

print(th8.name) 
# th8.name 就是 Neko("reimu").name  也就是 __init__中的self.name

th8.__init__("") #通过实例去执行 __init__  就是print("hello")

print(th8.__init__("")) #实例去执行 然后再打印这个实例,会出现none

th8.c("MuQ") #通过实例去执行函数c 并且赋值MuQ给 c_name
print(th8.c("MuQ"))  #实例去执行 然后再打印这个实例,会出现none

th8.n("Yakumo") #通过函数n赋值yakumo给neko_name,此时neko_name已经是self.name
print(th8.name) 

# def __init__(self):
#     selef.Data = []