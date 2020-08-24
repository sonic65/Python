def multiply(x):
    return (x * x)
def add(x):
    return (x + x)

funcs = [multiply, add]
for i in range(5):
    value = map(lambda x : x(i), funcs)
    print(list(value))

# 输出
# [x,  x[i]]
# [1, 2]
# [4, 4]
# [9, 6]