import requests
import json

def req_get(self,url,data):
    result = requests.get(url='http://www.weather.com.cn/weather1d/101020100.shtml',data='').text
    return result

# print(req_post(
#     None,
#     url='http://www.weather.com.cn/weather1d/101020100.shtml',
#     data='')
#     )


def req_post(self,url,data):
    result = requests.get(url=url,data=data)
    # res = json.dumps(result)
    return result

DATA = ''
URL = 'http://baidu.com'

print(req_post(
    None,
    URL,
    DATA)
    )