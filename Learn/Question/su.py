
# 算法题：输入字符串1：I have a student.；输入字符串2: aeiou； 处理：在字符串1中，将字符串2中的字母删掉；输出：I hv stdnt.
# # input("input a string: ")

x1 = "I hava a student"
x2 = "aeiou"

# x1a = '.'.join(x1)

# x2a = '.'.join(x2)

x1l = list(x1)
x2l = list(x2)

print(list(x1))
print(list(x2))

y  = x1.replace(x2,'',0)

print(y)


