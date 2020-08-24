l = []
for i in range(5):
    num = int(input("inpu a str: "))

    l.append(num)
    print(l)
    l1 = l.reverse()
    print(l1)

    l2 = l.sort()
    print(l2)

    lll = l1 + l2
    ll = l1.extand(l2)
    print(ll)


    for i in range(len(ll)):
        print(ll[i])
