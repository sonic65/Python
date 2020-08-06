import re

string1 = input('Input a tuple: ')
l = string1.split(",")
print(l)

t = re.findall(r'[0-9]+',string1)
k = tuple(t)
print(k)

print(t)