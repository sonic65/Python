
a = 100

print('a',id(a))
print(a)

def f1(n):
    print('n',id(n))
    n = n + 200
    print('n',id(n))
    print(n)

f1(a)
print('a',id(a))