from say_hello_deco import say_hello

@say_hello("china")
def american():
    print("I come from American")

@say_hello("american")
def chinese():
    print("我来自中国")

if __name__ == '__main__': 
    american()
    print("-----")
    chinese()