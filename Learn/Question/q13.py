import time
import datetime

print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print(time.localtime)

print(datetime.datetime.now())

print(time.strftime("%Y.%m.%d %H-%M-%S"))