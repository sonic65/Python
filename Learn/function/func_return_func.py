def hi(name="sonic"):
    def greet():
        return "in greet()"
    
    def welcome():
        return "in welcome()"
    
    if name == "sonic":
        return greet
    else:
        return welcome


# 返回greet ｜ 默认参数 name="sonic"，
# a = hi()
# print(a)

# 返回welcome 
# a = hi(name = "ali")
# print(a)

# 返回greet和welcome，而不是greet()和welcome()。
# 为什么那样？这是因为当你把一对小括号放在后面，这个函数就会执行；
# 然而如果你不放括号在它后面，那它可以被到处传递，并且可以赋值给别的变量而不去执行它。

# hi()返回greet函数 | hi()()返回 greet的执行结果 greet()
a = hi()
print(a)
print(a())