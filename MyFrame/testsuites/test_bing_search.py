# coding=utf-8
import time
import unittest
import os
import sys   
sys.path.append('/Users/sonic/Project/Python/MyFrame/')

from common.browser_engine import BrowserEngine
from pageobject.bing_homepage import HomePage
 
 
class BingSearch(unittest.TestCase):
 
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
 
    def tearDown(self):
        self.driver.quit()
 
    def test_bing_search(self):

        homepage = HomePage(self.driver)

        homepage.type_search1('')
        homepage.type_clear()
        homepage.est_click()
        homepage.type_search2('')

        homepage.search_btn()
        time.sleep(3)
        homepage.get_windows_img()
        time.sleep(3)

        try:
            assert 'python - 国际版 Bing' in self.driver.title
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))
 
if __name__ == '__main__':
    unittest.main()