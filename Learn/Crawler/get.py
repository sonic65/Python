from urllib.request import Request,urlopen
from urllib.parse import quote

print(quote("pyhon"))
url = "https://www.baidu.com/s?wd=python"

headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

request = Request(url,headers=headers)

response = urlopen(request)

print(response.read().decode())