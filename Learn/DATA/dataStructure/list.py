#list.append(x) 把X添加到list末尾
list = [1,2,3,4]

list.append(6)
print(list)

#list.insert(i,x) inster x to list at i
list.insert(0,"x")
print(list)

#list.extend(L) add all
list.extend("L")
print(list)

#list.pop([i]) remove 【i】
list.pop(2)
print("pop",list)

'''
#list.clear() remove all
list.clear()
print(list)
'''

#list.index(x) return first index x
list.index("x")
print("index",list)

#list.count count x in list
print(list.count("x"))

#list.remove(x) remove fist element named x
list.remove("x")
print(list)

list = [1,2,3,4,9,0,-1]
list.sort()
print("sort",list)

list.reverse()
print(list)

list.copy()
print(list)