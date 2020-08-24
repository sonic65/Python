#剔除字符串



x1 = "I am an engineer"
x2 = 'nm'

x1l = list(x1)
print(x1l)

x2l = list(x2)
print(x2l)

# # for i in range(x1l):
# #     while x1l[i] =

# x3 = x1.replace(x2l[1],'',100).replace(x2l[0],'',100)
# print(x3)

def replace_str():

    for i in range(0,len(x2l)):
        print(x2l[i])
        x3 = x1.replace(x2l[i],'',100)
        print(x3)
        
replace_str()