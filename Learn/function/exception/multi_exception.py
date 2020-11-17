# 所有可能发生的异常放到一个元组里
try:
    file = open('test.txt', 'rb')
except (IOError, EOFError) as e:
    print("An erroe occurred. {}".format(e.args[-1]))


# 对每个单独的异常在单独的except语句块中处理
try:
    file = open('test.txt', 'rb')
except EOFError as e:
    print("An EOF error occurred.")
    raise e
except IOError as e:
    print("An error occurred.")
    raise e

# 捕获所有异常
try:
    file = open('test.txt', 'rb')
except Exception:
    # 打印一些异常日志，如果你想要的话
    raise

# 包裹到finally从句中的代码不管异常是否触发都将会被执行
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
finally:
    print("This would be printed whether or not an exception occurred!")

