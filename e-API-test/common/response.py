import string
from urllib.parse import quote
import ssl
import urllib.parse
import urllib.request
import urllib
import re
import requests
import json

from requests.models import Response

host = 'https://janus.itest.talcloud.com'
service = '/epg-xkt-resource-library'
path = '/book/bookPage/list'

headers = {'Content-Type': 'application/json'}
# headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

data = {
    "bookId": 66353,
    "chapterId": 522930
}

method = 'POST'

url = host + service + path

# res = requests.request(method=method, url=url, json=data)

# # <Response [200]> type:class 'requests.models.Response
# # print(res)

# # 未解密的响应文档信息 type:bytes
# # print(res.content)

# # 解密过的文档信息 type:str
# # print(res.content.decode())

# # 解密过的文档信息 type:text
# # print(res.text)

# # json格式输出 type:dict
# # print(res.json())

# # # 转化成json格式 type:str
# # res_json = json.dumps(res.json())
# # # # print(res_json)

# # # 解码json格式 type:dict
# # res_dict = json.loads(res_json)
# # print(res_dict['status'])

# # 不知道是啥 type:str
# # res_to_json = json.dumps(res.content.decode('utf-8'))
# # print(res_to_json)
# # print(type(res_to_json))

# # url2 = res_json['url']

# # print(url2)

# # data2 = {
# #     "bookId": 66353,
# #     "chapterId": 522930
# # }

#####urllib######

ssl._create_default_https_context = ssl._create_unverified_context

url = host + service + path
url2 = 'http://baidu.com'
headers = {"Content-Type": "application/x-www-form-urlencoded"}

# python3处理含有中文的url  url=quote(url, safe=string.printable)
# 发起请求

data1 = {"bookId": 66353,"chapterId": 522930}

# data = str(data1)
# print(type(data1))
# # json.dumps(data)
# data2 = json.dumps(data)
# data3 = data1.encode('utf-8')
# print(data1)

# 写入josn文件
# with open(r'../common/data_json.json', 'w+') as f:
#     json.dump(data1 ,f)
#     print(data1)

# 读取json文件
with open(r'../common/temp.json', 'r+') as f:
    data5 = json.load(f)
    print(data5)

# data6 = json.dumps(data5)

# print(data6)
# data=data5.encode('utf-8')
# print("data",data)

data_json = json.dumps(data1)
print("data_json:", data_json)

# url参数化 结果：bookId=66353&chapterId=522930
# data_str = urllib.parse.urlencode(data_json).encode('utf-8')
# print(data_str)

# 字符串序列化
data_bytes = bytes(data_json, encoding='utf-8')
print("data_bytes:", data_bytes)

# 问题：如果接口只接收json格式，而urllib只只发送bytes形式
# req = urllib.request.Request(url=quote(url, safe=string.printable), data=data_bytes, headers=headers, method=method)
# res = urllib.request.urlopen(req, data=None, timeout=2, cafile=None, capath=None, cadefault=False, context=None)

# # # print(res.status)
# # print(res.getcode())
# # print(res.version)
# # print(res.reason)
# # print(res.geturl())
# # # print(res.info)
# # # 读取响应体
print(res.readline().decode('utf-8'))
# # print(res.read().decode('utf-8'))