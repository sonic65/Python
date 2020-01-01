# coding=utf-8
import time
import unittest
import os
import sys   
sys.path.append('/Users/sonic/Project/Python/MyFrame/common')
from common.browser_engine import BrowserEngine
from pageobject.bing_article_page import ArticleHomePage
 
 
class BingArticle(unittest.TestCase):
 
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
 
    def tearDown(self):
        self.driver.quit()
 
    def test_enter_article(self):

        homepage = ArticleHomePage(self.driver)
        homepage.click_article()
        time.sleep(3)
        homepage.get_windows_img()
        time.sleep(3)    

        try:
            assert 'Bing 学术' in self.driver.title
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))
 
if __name__ == '__main__':
    unittest.main()