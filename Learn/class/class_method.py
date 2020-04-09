class Tool(object):

    count = 0

    @classmethod
    def show_tool_count(cls):

        print("工具对象现在的数量是 %d"% cls.count)


    def __init__(self,name):
        self.name = name

        Tool.count += 1

tool1 = Tool("x") 
tool2 = Tool("a")

Tool.show_tool_count()


