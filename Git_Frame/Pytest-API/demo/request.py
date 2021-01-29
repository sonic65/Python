import json
import hashlib
from xlutils.copy import copy

import xlrd,xlwt
import conf
import requests
import json
import time,sys

basurl = 'http://'


class HttpRequest(object):

    def __init__(self, case):
        self.case = case
        try:
            self.case_expect = json.loads(self.case['case_expect'])
        except:
            self.case_expect = self.case['case_expect']
        print(case)

    def get_response(self):  # 获取请求结果
        response = self.send_request()
        return response

    def send_request(self):  # 发送请求

        try:

            rb = xlrd.open_workbook(conf.TEST_CASE_PATH)
            wb = copy(rb)
            sheet = rb.sheet_by_index(0)
            wbsheet = wb.get_sheet(0)
            rows = sheet.nrows
            cols = sheet.ncols

            for row in range(1, rows):
                print('----------------------------------当前执行--------第', row, '行----------------------------------')
                res = None
                url = sheet.row_values(row, 2, 3)[0]
                headers = {"User-Agent": "Chrome/51.0.2704.103"}

                method = sheet.row_values(row, 4, 5)[0]
                params = sheet.row_values(row, 5, 6)[0]

                res = requests.request(
                    method=method,
                    url=url,
                    headers=headers,
                    params=params
                    )
                if(res != None):
                    code = res['code']
                    msg = res['message']
                    wbsheet.write(row, 9, code)
                    wbsheet.write(row, 10, str(msg))
                    res=None
                    data_json=None
            wb.save(conf.TEST_CASE_PATH)

        except BaseException as e:
            print("Unexpected error:", sys.exc_info()[0], sys.exc_info()[1])
            print('发生异常')
        else:
            print('未发生异常')

    def check_response(self, response):
        response = response.json()

        if response == '<Response [200]>':
            return 'Y'
        else:
            return 'N'


if __name__ == '__main__':
    HttpRequest.send_request(1)