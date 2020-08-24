#题目：数字比较。

i = int(input("number1:"))
j = int(input("number2:"))

if i > j:
    print(i,">",j)
elif i == j:
    print(i,"=",j)
elif i< j:
    print(i,"<",j)
else:
    print("done")