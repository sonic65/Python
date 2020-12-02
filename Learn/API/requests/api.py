import requests
import requests
import json

def get(self,url,data):
    result = requests.get(url=url,data=data).json()
    res = result.dumps()
    return res

get(self, url, data)
