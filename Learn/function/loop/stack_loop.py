def test01(n):
    print("test01:",n)

    if n == 0:
        print("over")
    
    else:
        test01(n-1)
    
    print("stack的先进后出:",n)

test01(3)