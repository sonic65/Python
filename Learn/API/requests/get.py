import requests

# req = requests.request('GET','http://baidu.com')

req = requests.get('http://baidu.com')

print(req)
print(req.text)
print(req.json)
print(req.content.decode())