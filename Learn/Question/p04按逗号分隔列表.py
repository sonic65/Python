l = [1,23,4,5,6,7,8,"tr"]

for i in range(len(l)):
    # print(l[i])
    print(l[i],end=',')

# print(l.split(","))

S = ','.join(str(n) for n in l)
print(S)