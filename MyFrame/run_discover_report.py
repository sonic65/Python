import sys   
sys.path.append('/Users/sonic/Project/Python/MyFrame/common')
import HTMLTestRunner
import os
import unittest
import time


# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/Myframe/report/'
# print(report_path)

# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
# print(now)

# 设置报告名称格式
report_name = report_path + now + "_report.html"
fp = open(report_name, "wb")

# 构建suite
#定义要执行的测试用例的路径和名称格式
suite = unittest.TestLoader().discover("testsuites",pattern='test_*.py')


if __name__ =='__main__':
    
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(
        # 指定测试报告的文件
        stream=fp,
        # 测试报告的标题
        title=u"MyFrame 测试报告",
        # 测试报告的副标题
        description=u'用例执行情况（MacOS 64）'
    )
    runner.run(suite)