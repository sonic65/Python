#题目：输出 9*9 乘法口诀表。

for i in range (0, 10):
    # x = i * (i+1)
    # print()
    for j in range (1,i+1):
        # print(i,'x',j,'=',i*j)
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()   