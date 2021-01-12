#sonic账号地址
APP_ID = '20545078'
API_KEY = 'qROAdLBMg7msxQgCB5FBwXIc'
SECRECT_KEY = '2KEtyNrmIstLt48hzMvnAXaNMQKg88a6'

import re

def identify_words(index=0):
    from aip import AipOcr
    client = AipOcr(APP_ID, API_KEY, SECRECT_KEY)
    with open(r'./screen_capture/capture_code.png', 'rb') as f:
        img = f.read()
    message = client.basicGeneral(img)
    res = message['words_result']
    res1 = res[index]['words']

    """去除多余空格"""
    strinfo = re.compile(' ')
    res2 = strinfo.sub('', str(res1))
    return res2

if __name__ == '__main__':
    identify_words()