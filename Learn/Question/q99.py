fp = open('test.txt')
a = fp.read()
fp.close()

fp = open('test.txt')
b = fp.read()
fp.close


fp = open('test.txt','w')
c = a + b
fp.write(c)
fp.close


fp = open('test.txt','r')
print(fp.read())
fp.close
