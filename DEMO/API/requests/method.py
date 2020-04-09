import requests
import json

def req_get(self,url,data):
    result = requests.get(url='http://www.weather.com.cn/weather1d/101020100.shtml',data='')
    res = result.text
    return res

# print(req_get(
#     None,
#     url='http://www.weather.com.cn/weather1d/101020100.shtml',
#     Data='')
#     )


def req_post(self,url,data):
    result = json.dumps(requests.post(url=url,data=data).json(),ensure_ascii=False, sort_keys=True, indent=2)
    return result

    # result = requests.post(url=url,Data=Data).json()
    # res = json.dumps(result,ensure_ascii=False, sort_keys=True, indent=2)
    # return res

DATA = ''
URL = 'http://127.0.0.1:8888/login?name=xiaoming&pwd=1112'

print(req_post(
    None,
    URL,
    DATA)
    )