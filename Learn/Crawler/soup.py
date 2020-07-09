import requests
from bs4 import BeautifulSoup

class downloader(object):

    def __init__(self):
        self.server = 'server'
        self.target = 'target'
        self.names = []            #存放章节名
        self.urls = []            #存放章节链接
        self.nums = 0    

    def get_contents(self, target):
        req = requests.get(url = target)
        html = req.text
        bf = BeautifulSoup(html,'lxml')
        texts = bf.find_all('div', id='ftConw')
        texts = texts[0].text.replace('\xa0'*8,'\n\n')
        print(texts)
        return texts

    def save_contents(self, name, path, text):
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name)
            f.writelines(text)

s = downloader()
t = "http://www.baidu.com"
c = s.get_contents(t)
print(type(c))
s.save_contents('a','t.txt',c)