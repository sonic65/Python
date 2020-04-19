while True:
    try:
        x = int(input("请输入一个数字: "))
        print("输入的数字:",x)
        if x == 88:
            print("exit")
            break
    except ValueError:
        print("您输入的不是数字，请再次尝试输入！")

    else:
        print("bye")

    finally:
        print("always bye")