import requests
import json
from bs4 import BeautifulSoup
import re

def get_picture():

    URL = "http://www.baidu.com"
    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    res = requests.get(url=URL, headers=headers, verify=False)
    # print(res.text)
    soup = BeautifulSoup(res.text,"lxml")
    imgset = soup.find_all('img',id="s_lg_img_new")
    print("imgset:", imgset)

    for img in imgset:
        img_url = img.get('src')
        '''
        通过re模块对url进行修整，去掉 // 
        value：是需要处理的内容
        replace() 去掉的内容
        re.sub('\W+', '', value).replace("_", '')
        '''
        img_url = re.sub('//', '' , img_url).replace('//', '')
        img_url = 'http://' + img_url

        #通过requests取得图片内容
        png =  requests.get(img_url)
        print("imgURL:", img_url)
        print(png)

        #.content 保存内容
        with open ('logo.png', 'ab+') as f:
            f.write(png.content)


get_picture()