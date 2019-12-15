import unittest,time
from selenium import webdriver
import os
import time

username = '//*[@id="app"]/div/section/div/div/section/section/div/label[1]/input'        
password = '//*[@id="app"]/div/section/div/div/section/section/div/label[2]/input'
login_btn = '//*[@id="app"]/div/section/div/div/section/section/div/button'
pw_btn = '//*[@id="app"]/div/section/div/div/section/section/button'
sms = '//*[@id="app"]/div/section/div/div/section/section/div/div[2]/input'
host = "https://sso.faas.beta.elenet.me/euc/#/"

class lonin_page(unittest.TestCase):
    def setUp(self):

        driver=webdriver.Chrome()
        driver.implicitly_wait(5)
        self.driver=driver
        driver.get(host)

        pw_Btn = driver.find_element_by_id('//*[@id="app"]/div/section/div/div/section/section/button')

        self.username = username
        # self.password = password
        # self.login_btn = login_btn
        # PW_BTD = self.pw_Btn
        # self.pw_Btn = pw_Btn
        # self.sms = sms
        
        driver=webdriver.Chrome()
        driver.implicitly_wait(5)

        password = '//*[@id="app"]/div/section/div/div/section/section/div/label[2]/input'
        input_password = driver.find_element_by_xpath(password)
        self.input_password = input_password


    def login(self):
        driver=webdriver.Chrome()
        driver.implicitly_wait(5)

        #定义一个var做为host，get(host)
        host = "https://sso.faas.beta.elenet.me/euc/#/"
        driver.get(host)
        #直接通过driver操作元素
        driver.find_element_by_class_name("tachyon-icon").click()

        #定义元素
        username = '//*[@id="app"]/div/section/div/div/section/section/div/label[1]/input'
        driver.find_element_by_xpath(username).send_keys('E010785')

        #定义动作
        lonin_page.setup.input_password.send_keys("123456")
       
        
        time.sleep(1)



        # driver.find_element_by_class_name(pwbtn).click()

        # pw_btn = driver.find_element_by_class_name(pw_btn)
        # pw_btn.click()
        #driver.find_element_by_class_name(pw_btn).click()

    # def login2(self):
    #     pw = "123456"
    #     self.input_password.send_keys(pw)
         
        

       # pw_Btn.click()
        # time.sleep(1)
        # driver.quit()  



        # driver.find_element_by_id(username).send_keys('E010785')
        # driver.find_element_by_id(password).send_keys("123456")
        # driver.find_element_by_id(sms).send_keys('1')

    def tearDown(self):
        self.driver.quit()     


    