#python 3.7
#https://yach-open-doc.zhiyinlou.com/server-api/robot/机器人开发.html#自定义机器人

import time
import hmac
import hashlib
import base64
import urllib.request
import json
import requests

secret = 'SEC9b3c574b1b4e6c6b66f44379ec62915e'
access_token = 'bDBWb2FPWjByUFdpSHROZ0IySjlpVFI4WTVIQmJkVEp2VDZrcXlvYk5mbkZkUmpmVW54c1ZMcjNOM2IvWlN4QQ'
host = 'https://yach-oapi.zhiyinlou.com/robot/send'

class ibot():

    def ibot_sign():
        timestamp = int(round(time.time() * 1000))
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.request.quote(base64.b64encode(hmac_code))
        return  timestamp , sign

    def ibot_request():
        headers = {"Content-Type":"application/json"}
        data = {
            "msgtype": "text",
            "text": {
                "content": "小R Flask"
            },
            "msgtype": "markdown",
            "markdown": {
                "title": "flask",
                "text": "小R from FLask # 这是支持markdown的文本 \n## 标题2  \n* 列表1 \n![alt 啊](https://www.xiaoheiban.cn/download/qrcode-android.svg)"
            }
        }
        method = 'POST'

        s = ibot.ibot_sign()
        timestamp = str(s[0])
        sign = s[1]
        url = host + '?' + 'access_token=' + access_token + '&' + 'timestamp' + '=' + timestamp + '&' + 'sign=' + sign

        res = requests.request(method=method, url=url, headers=headers, json=data)
        r = json.dumps(res.json())
        return r
        
if __name__ == "__main__":
    ibot.request()
