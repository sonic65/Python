#!/usr/bin/python3
#每个模块都有一个__name__属性
#当其值是'__main__'时，表明该模块自身在运行，否则是被引入。

if __name__ == '__main__':
    print("self running")
else :
    print("other running")