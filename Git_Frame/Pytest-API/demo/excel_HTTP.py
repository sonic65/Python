import hashlib
from xlutils.copy import copy

import xlrd,xlwt
import conf
import requests
import json
import time,sys


class ExcelHandler():

    def get_excel_data(self):
        try:
            header = {"User-Agent": "Chrome/51.0.2704.103"}

            rb = xlrd.open_workbook(conf.TEST_CASE_PATH)
            wb = copy(rb)
            sheet = rb.sheet_by_index(0)
            wbsheet = wb.get_sheet(0)
            rows = sheet.nrows
            ols = sheet.ncols
            '''
            print(sheet.row(0)) #第一页 第一列
            print(sheet.col(0)) #第一页 第一行
            '''
            for row in range(1, rows):
                print('----------------------------------当前执行--------第', row, '行----------------------------------')
                res = None
                url = sheet.row_values(row, 2, 3)[0]
                method = sheet.row_values(row, 4, 5)[0]
                params = sheet.row_values(row, 5, 6)[0]
                if (method == 'GET'):
                    if (params == None or params == ''):
                        res = self.get_invoke(url,params,header)
                    else:
                        res = self.get_invoke(url+'?'+params,None,header)
                else:
                    data_json = None
                    header['Content-Type']='application/json'
                    if(params != None and params != '' and len(params) !=0):
                        data_json = json.dumps(json.loads(params))
                    res = self.post_invoke(url, data_json, header)

                #返回所有结果
                # print('执行结果返回:',str(res))
                #返回code和message
                code = res['code']
                msg = res['message']
                print('测试接口：',url,'\n测试结果：code：',code,",“message：",msg)
                # print('测试接口：',url,'\n测试结果：',msg)

                if(res != None):
                    code = res['code']
                    msg = res['message']
                    wbsheet.write(row, 9, code)
                    wbsheet.write(row, 10, str(msg))
                    res=None
                    data_json=None
            wb.save(conf.TEST_CASE_PATH)

        except BaseException as e:
            print("Unexpected error:", sys.exc_info()[0],sys.exc_info()[1])
            print('发生异常')
        else:
            print('未发生异常')


    def post_invoke(self, url, data, headers=None):
        res = None
        if headers == None:
            res = requests.post(url=url, data=data)
        else:
            res = requests.post(url=url, data=data, headers=headers)
        return json.loads(res.content.decode())


    def get_invoke(self, url, data, headers=None):
        res = None
        if headers == None:
            res = requests.get(url=url, data=data)
        else:
            res = requests.get(url=url, data=data, headers=headers)
        return json.loads(res.content.decode())

    def token_md5(self):
        t = time.time()
        timeStamp = (round(t * 1000))
        signStr = '3825720472286642210' + "-" + '1515795216911630337' + "-" + str(
            timeStamp) + "-" + 'ee54bcd1-662c-47ae-8117-76946e3d4e1f'
        m1 = hashlib.md5()
        # 使用md5对象里的update方法md5转换
        m1.update(signStr.encode("utf-8"))
        signVal = m1.hexdigest()
        print(timeStamp, signVal)
        return signVal, str(timeStamp)

    def access_Token(self):
        pass

    def session(self):
        pass


if __name__ == '__main__':
    ExcelHandler().get_excel_data()
