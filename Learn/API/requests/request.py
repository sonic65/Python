timestamp = '1608625478301'
sign = 'r9BsOLcfJWcoK2EHdXs3fT7dGcx94s%2BG%2BCFWiSwk4os%3D'
host = 'https://yach-oapi.zhiyinlou.com/robot/send'
access_token = 'bDBWb2FPWjByUFdpSHROZ0IySjlpVFI4WTVIQmJkVEp2VDZrcXlvYk5mbkZkUmpmVW54c1ZMcjNOM2IvWlN4QQ'

url = host + '?' + 'access_token=' + access_token + '&' + 'timestamp' + '=' + timestamp + '&' + 'sign=' + sign

headers = {
    "Content-Type":"application/json"
}

data = {
    "msgtype": "text",
    "text": {
        "content": "小R"
    },

    "msgtype": "markdown",
    "markdown": {
        "title": "首屏会话透出的展示内容",
        "text": "小R # 这是支持markdown的文本 \n## 标题2  \n* 列表1 \n![alt 啊](https://www.xiaoheiban.cn/download/qrcode-android.svg)"
    }

}

method = 'POST'

import requests
print(url)
res = requests.request(method=method, url=url, headers=headers, json=data)
print(res.content.decode())