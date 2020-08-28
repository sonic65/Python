
def function1(func):
    def decorator():
        print("Before")
        func()
        print("After")
        return func
    return decorator

@function1
def function2():
    print("Hello Python")


function2()