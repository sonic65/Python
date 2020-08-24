some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)


# 重复值
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)


valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
# 差集
print(input_set.difference(valid))

# 交集
print(input_set.intersection(valid))