# -*- coding: utf-8 -*-
# __author__ = "maple"


'''

请求相关
'''
import hashlib
import json
import requests
from bs4 import BeautifulSoup
from LoggerHandler import logger
# from settings import conf
import urllib
import urllib.request
import urllib.parse
import time
import conf

class RequestHandler(object):

    def __init__(self, case):
        self.case = case
        try:
            self.case_expect = json.loads(self.case['case_expect'])
        except:
            self.case_expect = self.case['case_expect']

    @property
    def get_response(self):
        """ 获取请求结果 """
        response = self.send_request()
        return response

    #获取某个接口返回的结果
    # 此方法可以用来进行接口串联测试，来获取之前接口返回的值
    # 参数 path: excle路径
    # 参数 url:请求地址
    def get_url_response(self,path,url):
        read_excle_result = self.read_excle(path)
        for result in read_excle_result:
            if result['url'] == url:
                this_url_response = result['code']
                return this_url_response

    def token_md5(self):
        t = time.time()
        timeStamp = (round(t * 1000))
        signStr = '3825720472286642210' + "-" + '1515795216911630337' + "-" + str(
            timeStamp) + "-" + 'ee54bcd1-662c-47ae-8117-76946e3d4e1f'
        m1 = hashlib.md5()
        # 使用md5对象里的update方法md5转换
        m1.update(signStr.encode("utf-8"))
        signVal = m1.hexdigest()
        # print(timeStamp, signVal)
        return signVal, str(timeStamp)

    def send_request(self):
        """ 发请求 """
        try:
            sigRes = RequestHandler().token_md5()

            headers = {
                'Consumer_Service_Id': 3825720472286642210,
                'Provider_Domain_Id': 1515795216911630337,
                'Sig': sigRes[0],
                'Time_Stamp': sigRes[1],
                'Content-Type': 'application/json'
            }

            response = requests.request(
                method=self.case['case_method'],
                url=self.case['case_url'],
                data=self.case['case_params'],
                headers=headers
            )
            print(response)

            print(response.text)
            content_type = response.headers['Content-Type']
            content_type = content_type.split(";")[0].split('/')[-1] if ';' in content_type else \
            content_type.split("/")[-1]
            if hasattr(self, '_check_{}_response'.format(content_type)):
                response = getattr(self, '_check_{}_response'.format(content_type))(response)
                print(response)
            else:
                raise '返回类型为: {}, 无法解析'.format(content_type)
        except:
            logger().error({'response': "请求发送失败，详细信息： url={}".format(self.case['case_url'])})
            return {'response': "请求发送失败，详细信息： url={}".format(self.case['case_url'])}, self.case['case_expect']

        return response

    def _check_json_response(self, response):
        """  处理json类型的返回值 """
        response = response.json()  # {'success': True}
        for key in self.case_expect:
            if self.case_expect[key] != response[key]:  # 用例执行失败的
                return {key: self.case_expect[key]}, {key: response[key]}
        else:  # 执行成功
            logger("发送请求").info('{} 执行成功'.format(self.case['case_url']))
            return {key: self.case_expect[key]}, {key: response[key]}

    def _check_html_response(self, response):
        """ 校验html类型的数据"""
        soup_obj = BeautifulSoup(response.text, 'html.parser')
        title = soup_obj.find('title').text
        return title, self.case_expect

    def _check_params(self):
        """ 整理参数 """
        if self.case['case_params']:
            """
            做扩展
            """
            pass
        else:
            return {}

if __name__ == '__main__':
    RequestHandler().send_request()