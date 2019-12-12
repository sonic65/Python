# _thread.start_new_thread ( function, args[, kwargs] )

'''
参数说明:

function - 线程函数。
args - 传递给线程函数的参数,他必须是个tuple类型。
kwargs - 可选参数。
'''

#!/usr/bin/python

import _thread
import time

# def a function fo thread
def print_time (threadName,delay):
    count = 0
    while count < 5 :
        time.sleep(delay)
        count +=1
        print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

#creat two thread 
try:
    _thread.start_new_thread(print_time,("Thread-1",2,))
    _thread.start_new_thread(print_time,("Thread-2",4,))
except:
    print("error")

while 1:
    pass
