from selenium import webdriver
from base import BasePage #from文件名模块 import类
import time

class BaiduSearch(object):

    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    basepage = BasePage(driver)

    def open_baidu(self):
        self.basepage.open_url("http://baidu.com")
        time.sleep(1)

    def quit_baidu(self):
        self.basepage.quit_browser()


baidu = BaiduSearch()
baidu.open_baidu()