from say_hello_deco import say_hello

@say_hello("china")
def american():
    print("I come from American")

@say_hello("american")
def chinese():
    print("我来自中国")

def say_hello(contry):
    def wrapper(func):
        def deco(*args, **kwargs):
            if contry == "china":
                print("你好!")
            elif contry == "american":
                print('hello.')
            else:
                return

            # 真正执行函数的地方
            func(*args, **kwargs)
        return deco
    return wrapper


if __name__ == '__main__': 
    american()
    print("-----")
    chinese()