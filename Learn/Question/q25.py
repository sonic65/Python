#计算阶乘

n = int(input('input a number: '))
fac = 1

for i in range(1, n+1):
    fac = fac*i
    print(fac)
print(fac)