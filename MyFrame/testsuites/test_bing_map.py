# coding=utf-8
import time
import unittest
import os
import sys   
sys.path.append('/Users/sonic/Project/Python/MyFrame/')

from common.browser_engine import BrowserEngine
from pageobject.bing_map_page import MapHomePage
 
 
class BingMap(unittest.TestCase):
 
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
 
    def tearDown(self):
        self.driver.quit()
 
    def test_enter_map(self):
        homepage = MapHomePage(self.driver)
        homepage.click_map()
        time.sleep(3)
        homepage.get_windows_img()
        time.sleep(3)   

        try:
            assert 'Bing 地图' in self.driver.title
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))
 
if __name__ == '__main__':
    unittest.main()