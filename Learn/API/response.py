import re
import requests
import json

from requests.models import Response

host = 'https://janus '
service = '/ '
path = '/book/bookPage/list'

data = {
    "bookId": 66353,
    "chapterId": 522930
}

method = 'POST'

url = host + service + path

res = requests.request(method=method, url=url, json=data)


# <Response [200]> type:class 'requests.models.Response
# print(res)

# 未解密的响应文档信息 type:bytes
# print(res.content)

# 解密过的文档信息 type:str
# print(res.content.decode())

# 解密过的文档信息 type:text
# print(res.text)

# json格式输出 type:dict
# print(res.json())

# # 转化成json格式 type:str
# res_json = json.dumps(res.json())
# # # print(res_json)

# # 解码json格式 type:dict
# res_dict = json.loads(res_json)
# print(res_dict['status'])

# 不知道是啥 type:str
# res_to_json = json.dumps(res.content.decode('utf-8'))
# print(res_to_json)
# print(type(res_to_json))


# url2 = res_json['url']

# print(url2)

# data2 = {
#     "bookId": 66353,
#     "chapterId": 522930
# }

#####urllib######

import urllib
import urllib.request
import urllib.parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import json

url = host + service + path
url2 = 'http://baidu.com'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

#python3处理含有中文的url  url=quote(url, safe=string.printable)
from urllib.parse import quote
import string
# 发起请求

data1 = {
    "bookId": 66353,
    "chapterId": 522930
}
data = str(data1)

req = urllib.request.Request(url=quote(url, safe=string.printable), data=data.encode('utf-8'), headers=headers, method=method) 
res = urllib.request.urlopen(req, data=None, timeout=2, cafile=None, capath=None, cadefault=False, context=None)

# print(res.status)
# print(res.getcode())
# print(res.version)
# print(res.reason)
# print(res.geturl())
# print(res.info)
# 读取响应体
print(res.readline().decode('utf-8'))
print(res.read().decode('utf-8'))