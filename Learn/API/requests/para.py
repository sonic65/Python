import requests
import json

data1 = {}

proxies = {
  "http": "http://12.34.56.79:9527",
  "https": "http://12.34.56.79:9527",
}

method = 'GET'

URL = 'http://www.weather.com.cn/weather1d/101020100.shtml'

headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

response = requests.request(method=method,url = URL,json = data1,headers = headers,proxies = '')

print(response)
print(response.text)




# 环境变量代理
# export HTTP_PROXY="http://12.34.56.79:9527"
# export HTTPS_PROXY="https://12.34.56.79:9527"


