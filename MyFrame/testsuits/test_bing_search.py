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
        time.sleep(1)

        # homepage.type_search('123')
        # time.sleep(3)

        # homepage.type_clear()
        # # homepage.est_click()
        # time.sleep(3)

        homepage.type_search('333')

        homepage.search_btn()
        time.sleep(10)


        # homepage.send_submit_btn()
        # time.sleep(3)
        homepage.get_windows_img()

        try:
            assert 'selenium' in self.driver.title
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))
 
if __name__ == '__main__':
    unittest.main()