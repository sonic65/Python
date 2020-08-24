#阶乘

#1 递归
def fact(j):
    sum = 0
    if j == 0 :
        sum = 1
    else:
        sum = j * fact(j - 1)
    return sum

print(fact(int(input('input a number: '))))



#2 
# def fact(x):
#     if x == 0 :
#         return 1
#     return x * fact(x - 1)

# x = int(input('Input a number: '))

# print(fact(x))

#3
for letter in 'Python':
    print(letter)