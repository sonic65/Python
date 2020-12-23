#python 3.7
#https://yach-open-doc.zhiyinlou.com/server-api/robot/机器人开发.html#自定义机器人

import time
import hmac
import hashlib
import base64
import urllib.request

timestamp = int(round(time.time() * 1000))
secret = 'SEC9b3c574b1b4e6c6b66f44379ec62915e'
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.request.quote(base64.b64encode(hmac_code))
print(timestamp)
print(sign)
