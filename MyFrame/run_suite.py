
import unittest
import testsuites
from testsuites.test_bing_article import BingArticle
from testsuites.test_bing_map import BingMap
from testsuites.test_bing_search import BingSearch


 
# suite = unittest.TestSuite(unittest.makeSuite(BingArticle))
suite = unittest.TestSuite(unittest.makeSuite(BingMap))
# suite = unittest.TestSuite(unittest.makeSuite(BingSearch))

 
if __name__=='__main__':
    #执行用例
    runner=unittest.TextTestRunner()
    runner.run(suite)