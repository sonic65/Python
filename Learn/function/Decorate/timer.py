import time

# 这是装饰函数
def timer(func):
    def wrapper(*args, **kw):
        t1=time.time()
        # 这是函数真正执行的地方
        func(*args, **kw)
        t2=time.time()
        # 计算下时长
        cost_time = t2-t1 
        print("花费时间：{}秒".format(cost_time))
    return wrapper

import time
@timer  #相当于 time = timer(want_sleep(10)
def want_sleep(sleep_time):
    time.sleep(sleep_time)

want_sleep(10) 















def deco(func):
    t1 = time.time
    func()
    t2 = time.time
    t = t2 - t1
    print(t)

    return func













