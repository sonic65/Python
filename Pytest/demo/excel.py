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
                        res = self.send_request(url,params,header)
                    else:
                        res = self.send_request(url+'?'+params,None,header)
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


    def send_request(self):
        """ 发请求 """
        try:
            response = requests.request(
                method=self.case['case_method'],
                url=self.case['case_url'],
                params=self._check_params()
            )
            content_type = response.headers['Content-Type']
            content_type = content_type.split(";")[0].split('/')[-1] if ';' in content_type else \
            content_type.split("/")[-1]
            if hasattr(self, '_check_{}_response'.format(content_type)):
                response = getattr(self, '_check_{}_response'.format(content_type))(response)
            else:
                raise '返回类型为: {}, 无法解析'.format(content_type)
        except:
            logger().error({'response': "请求发送失败，详细信息： url={}".format(self.case['case_url'])})
            return {'response': "请求发送失败，详细信息： url={}".format(self.case['case_url'])}, self.case['case_expect']

        return response

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


if __name__ == '__main__':
    ExcelHandler().get_excel_data()
