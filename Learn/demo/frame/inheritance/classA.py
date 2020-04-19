from selenium import webdriver
import time

class ClassA(object):

    def open_baidu(self):

        driver = webdriver.Chrome()
        driver.get("http://baidu.com")
        time.sleep(4)
        driver.quit()