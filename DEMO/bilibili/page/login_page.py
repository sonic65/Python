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
login_id = '//*[@id="geetest-wrap"]/ul/li[5]/a[1]'

user1 = "淡い柠檬草"
pw1 = "56749154bB"


class Lonin_Page(unittest.TestCase):
    def setUp(self):

        driver=webdriver.Chrome()
        driver.implicitly_wait(5)
        self.driver=driver

        # 公共操作 
        driver.get(host)
        driver.find_element_by_class_name("name").click()

        name = driver.find_element_by_xpath(username)
        word = driver.find_element_by_xpath(password)
        logon = driver.find_element_by_xpath(login_id)
        self.NAME = name
        self.PW = word
        self.Logon = logon


    def tearDown(self):
        self.driver.quit()    
    
    # def switch_window(self):
    #     #切换窗口
    #     for handle in self.driver.window_handles:
    #         self.driver.switch_to.window(handle)
    #         #j增加等待时间，可以提高测试用例执行的健壮性
    #         time.sleep(2)
    #     time.sleep(3)        

    def test_login(self):
        self.NAME.send_keys(user1)
        self.PW.send_keys(pw1)
        self.Logon.click()
        time.sleep(5)

        try:
            assert '哔哩哔哩1' in self.driver.title
            print('pass')
        except Exception as e:
            print('failure',format(e))

bilibili = Lonin_Page()
bilibili.setUp()            


    