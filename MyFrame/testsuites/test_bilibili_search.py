# coding=utf-8
import time
import unittest
import os
import sys   
sys.path.append('/Users/sonic/Project/Python/MyFrame/')

from common.browser_engine import BrowserEngine
from pageobject.bilibili_homepage import HomePage
 
 
class Test_Bilibili_Home(unittest.TestCase):
 
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def tearDown(self):
        self.driver.quit()
 
    def test_bilibili_search(self):

        homepage = HomePage(self.driver)
        time.sleep(3)
        homepage.login_click()
        # time.sleep(3)
        # homepage.user_name_type('123')
        # time.sleep(3)
        # homepage.user_password_type('123')
        time.sleep(3)
        homepage.login_btn_click()
        time.sleep(3)

        try:
            assert 'selenium' in self.driver.title
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))
 
if __name__ == '__main__':
    unittest.main()