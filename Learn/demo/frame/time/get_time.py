import time;

class GetTime(object):

    def get_sys_time(self):
        print(time.time())
        print(time.localtime())
        new_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print(new_time)

t = GetTime()
t.get_sys_time()