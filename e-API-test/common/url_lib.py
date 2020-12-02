url3 = 'https://epg-xkt.oss-cn-shanghai.aliyuncs.com/user/206848/822657/202011/f8f588cd436a43f183ffa2533562ba32/9-25.doc'
url4 = 'https://epg-xkt.oss-cn-shanghai.aliyuncs.com/user/10055/852926/20209/57e944f8a19246d1b3c8d7e496e4a74e/Read%20a%20story2020-09-27.doc'

import urllib
import urllib.request
import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import json

res = urllib.request.urlopen(url4, data=None, timeout=2, cafile=None, capath=None, cadefault=False, context=None)

print(res.status)
print(res.getcode())
print(res.version)
print(res.reason)
print(res.geturl())
print(res.info)

# 读取响应体
# print(res.readline().decode('utf-8'))
# print(res.read().decode('utf-8'))
