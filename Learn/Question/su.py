
# 算法题：输入字符串1：I have a student.；输入字符串2: aeiou； 处理：在字符串1中，将字符串2中的字母删掉；输出：I hv stdnt.
# # input("input a string: ")

x1 = "I hava a student"
x2 = "aeiou"

x1a = '.'.join(x1)
print(x1.split())
print(x1a)

x2a = '.'.join(x2)

print(x2a)

y  = x1a.replace(x2a,'',0)

print(y)


#倒序数字
# x = input('input a number: ')
# y = list(x)
# print(y)

# z = y.reverse()

# print(z)
