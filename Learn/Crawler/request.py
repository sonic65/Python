import requests
import re

url = "http://wwww.bilibili.com"

headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
            
}


response = requests.get(url,headers=headers)

# info = response.read()
info = response.text

infoa = re.findall(r'<div class="content"><span>+</span>',info)

print(infoa)

with open('baiducontent.txt','w',encoding='utf-8') as f:
    f.write(str(infoa))