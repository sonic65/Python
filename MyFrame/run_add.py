import unittest
import testsuites
from testsuites.test_bing_article import BingArticle
from testsuites.test_bing_map import BingMap
from testsuites.test_bing_search import BingSearch
import time,os


import sys   
sys.path.append('/Users/sonic/Project/Python/MyFrame/common')
from common.HTMLTestRunner import HTMLTestRunner

#TestSuit()
#初始化一个suite实例，然后这个实例有一个addTest()的方法,可以加载不同类里面的不同测试函数，
#addTest(测试类的类名（‘测试函数名称，就是test开头的函数’）)，

suite = unittest.TestSuite()
suite.addTest(BingArticle('test_enter_article'))
# suite.addTest(BingMap('test_enter_map'))
# suite.addTest(BingSearch('test_bing_search'))

report_path = os.path.dirname(os.path.abspath('.')) + '/Myframe/report/'
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
report_name = report_path + now + '_report.html'
fp = open(report_name, "wb")

if __name__ =='__main__':
    
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u"MyFrame 测试报告",
        description=u'用例执行情况（Mac OS）'
    )
    runner.run(suite)