import unittest
import testsuites
from testsuites.test_bing_article import BingArticle
from testsuites.test_bing_search import BingSearch
from testsuites.test_bing_map import BingMap

suite = unittest.TestSuit
#TestSuit
#suite实例 addTest(测试类的类名（‘测试函数名称，就是test开头的函数’）)
suite.addTest(BingArticle('test_enter_article'))
suite.addTest(BingSearch('test_bing_search'))
suite.addTest(BingMap('test_enter_map'))

if __name__=='__main__':

    runner=unittest.TextTestRunner()