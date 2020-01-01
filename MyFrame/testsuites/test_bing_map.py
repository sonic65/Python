# coding=utf-8
import time
import unittest
import os
import sys   
sys.path.append('/Users/sonic/Project/Python/MyFrame/')

from common.browser_engine import BrowserEngine
from pageobject.bing_homepage import HomePage
 
 
class BingMap(unittest.TestCase):
 
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
 
    def tearDown(self):
        self.driver.quit()
 
    def test_enter_map(self):
        self.click_map()

        try:
            assert 'Bing 地图' in self.driver.title
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))
 
if __name__ == '__main__':
    unittest.main()