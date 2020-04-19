#raise  自定义异常,
# 语句抛出一个指定的异常。
#raise [Exception [, args [, traceback]]]

x = 10
if x > 5:
    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))