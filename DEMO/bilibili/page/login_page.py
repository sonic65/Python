import unittest,time
from selenium import webdriver
import os
import time

host = "https://www.bilibili.com/"
login = '//*[@id="internationalHeader"]/div[1]/div/div[3]/div[2]/div[1]/div/span/div/a'

username = '//*[@id="login-username"]'        
password = '//*[@id="login-passwd"]'
login_btn = '//*[@id="geetest-wrap"]/ul/li[5]/a[1]'
scroll = ''

user1 = "lemon"

class lonin_page(unittest.TestCase):
    def setup(self):

        driver=webdriver.Chrome()
        driver.implicitly_wait(5)
        self.driver=driver
        
        # 公共操作 
        driver.get(host)
        driver.find_element_by_xpath().click(login)
        name = driver.find_element_by_xpath('//*[@id="login-username"]')
        self.name = name

    def tearDown(self):
        self.driver.quit()    

    def login(self):
        self.name.send_keys("lemon")




    