
def deco(contry):
    def wrapper(func):
        def de(*args, **kwargs):
            if contry == "China":
                print("你好，这是：")
            elif contry == "American":
                print("Hello, this is: ")
            else:
                return
            
            func(*args, **kwargs)
        return de
    return wrapper

@deco("China")
def Chinese():
    print("Python")

@deco("American")
def American():
    print("Python")

if __name__ == "__main__":
    # American()
    Chinese()