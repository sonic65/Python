string = input('Input a string: ')
stringA = string.upper()
print(stringA)

fp = open('test.txt','w')
# print(fp.read())
fp.write(stringA)

fp = open('test.txt','r')
print(fp.read())
fp.close()