import csv

filename='/Users/gaoyuhang/Project/Python/work/list.csv'

f=open(filename)

arr = []
for line in f.readlines():
  line=line.strip()
  print(line)
  for x in line.split(' '):
    arr.append(x)
print(arr)
# print("\n".join(arr))

