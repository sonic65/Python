import time

def deco(func):
    def wrapper(*args):
        t1 = time.time()
        func(*args)
        t2 = time.time()
        t = t2 - t1
        print(t)
    return wrapper

# f = time.sleep(3)
# print(f)

@deco
def t(n):
    time.sleep(n)

t(0)