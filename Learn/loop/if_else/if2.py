#!/usr/bin/python3

age = int(input("input your cat's age:"))
print("")
if age <= 0:
    print("are you kidding?")
elif age == 1:
    print("age is 1")
elif age == 2:
    print("she is adult")
elif age > 2:
    human = 22 + (age -2)*5
    print("age is ",human,"like man")

### 推出提示
input("press enter to exit")