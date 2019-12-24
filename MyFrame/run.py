import unittest

import sys   
sys.path.append('/Users/sonic/Project/Python/MyFrame/common')
from common.HTMLTestRunner import HTMLTestRunner
#导入HTMLTestRunner的包
#导入test_login的包，执行测试用例时需使用

#定义要执行的测试用例的路径
test_dir = './testsuites'
#定义要执行的测试用例的路径和名称格式
suite = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

#test_*.py的意思是，./testcase路径下文件名称格式为test_*.py的文件，*为任意匹配，路径下有多少的test_*.py格式的文件，就依次执行几个
#定义测试报告的名称和存储位置
filename = './report/loginReport.html'

if __name__=='__main__':
    #执行用例
    runner=unittest.TextTestRunner()
    runner.run(suite)

    #以wb(可写的二进制文件)形式，打开文件，若文件不存在，则先执行创建，再执行打开
    fp = open(filename, 'wb')
    #调用HTMLTestRunner生成报告
    runner = HTMLTestRunner.HTMLTestRunner(
        # 指定测试报告的文件
        stream=fp,
        # 测试报告的标题
        title=u"MyFrame 测试报告",
        # 测试报告的副标题
        description=u'用例执行情况（win10 64位）'
    )
    #执行用例

