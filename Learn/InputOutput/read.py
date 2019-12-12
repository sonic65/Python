f = open("file.txt","r")

str = f.read()
print(str)

str1 = f.readline()
print(str1)

str2 = f.readlines()
print(str2)
f.close()