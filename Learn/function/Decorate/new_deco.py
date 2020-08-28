def new_decorator(a_func):

    def wrap_func():
        print("Before a_func()")
        a_func()
        print("After a_func()")
    return wrap_func

def requiring_decoration():
    print("Needs decorator")
    return 1

# 以下两种情况输出”Needs decorator“，很好理解
# requiring_decoration()
# print(requiring_decoration())
# new_decorator(requiring_decoration)()
# print(new_decorator(requiring_decoration)())

# requiring_decoration 表示该函数
# new_decorator(requiring_decoration) 表示new_decorator函数的返回值
# print(requiring_decoration)

# new_decorator return wrap_func 该函数就是 wrap_func
# print(new_decorator(requiring_decoration))

# print(new_decorator(requiring_decoration))
# requiring_decoration = new_decorator(requiring_decoration)
# requiring_decoration()

@new_decorator
def requiring_decoration():
    """Decorate"""
    print("I am the function which needs some decoration")

requiring_decoration()
print(requiring_decoration)
print(requiring_decoration.__name__)

