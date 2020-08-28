def country_choose(country):
    def decorator(fun_need_deco):
        def wrap_fun(*args):
            if country == "American":
                print("Hello")
            elif country == "China":
                print("你好")
            else:
                print("Hello")
            return fun_need_deco(*args)
        return wrap_fun
    return decorator


def hello_python():
    print("python")

@country_choose("China")
def hello_python_China():
    print("python")

@country_choose("American")
def hello_python_American():
    print("python")

@country_choose("England")
def hello_python_England():
    print("python")

if __name__ == '__main__':
    hello_python_American()
    hello_python_China()
    hello_python_England()