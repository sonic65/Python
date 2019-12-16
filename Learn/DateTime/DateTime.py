#!/usr/bin/python3

import time;  # 引入time模块

ticks = time.time()

print ("当前时间戳为:", ticks)
print(time.time())
print(time.localtime())
new_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print(new_time)
