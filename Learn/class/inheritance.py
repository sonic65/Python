class Cat(object):
    leg = 4

    def __init__(self,neko_name):
        self.name = neko_name
        print(neko_name)

    def miao(self):
        print("miao")    


class RagCat(Cat):
    def __init1__(self, neko_name):
        super().__init__(neko_name)

    def eye(self):
        print("nice") 
    
th8 = Cat("chen")
th9 = RagCat("lan")
th9.eye()
th9.__init1__("1")
th9.__init__("1")



