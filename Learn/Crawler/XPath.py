
import urllib
from urllib.request import urlopen

url = "http://www.baidu.com"

urlopen(url)

response = urlopen(url)

info = response.read()

print(info.decode())

xpath('div/*')