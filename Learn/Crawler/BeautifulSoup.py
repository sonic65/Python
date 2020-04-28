import requests
import re
from bs4 import BeautifulSoup
import parser

url = "https://www.ttdytt.cc/kehuandianying/"

headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

response = requests.get(url,headers=headers)
info = response.text

soup = BeautifulSoup(info)
print(soup.title)
print(soup.div)
print(soup.div.get('class'))
# print(soup.div['float'])
# print(soup.a['href'])
print(soup.div.text)

print(soup.find_all('title'))
# print(soup.find_all('div',_class=))

print("--------------css()--------------")
print(soup.select('title'))
print(soup.select('div > span'))

with open("beautiful.txt",'w') as f:
    f.write(str(soup))