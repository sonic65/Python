from urllib.request import Request
from urllib.request import urlopen

url = "http://wwww.baidu.com"

headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}


request = Request(url,headers=headers)

response = urlopen(url)

info = response.read()

print(info.decode)