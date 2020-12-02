# coding=utf-8
from common.base_page import BasePage
import time
 
 
class HomePage(BasePage):
    
    login = 'xpath=>//*[@id="internationalHeader"]/div[1]/div/div[3]/div[2]/div[1]/div/span/div/a'

    username = 'xpath=>//*[@id="login-username"]'        
    password = 'xpath=>//*[@id="login-passwd"]'
    login_btn = 'xpath=>//*[@id="geetest-wrap"]/ul/li[5]/a[1]'
    scroll = ''
    login_id = 'xpath=>//*[@id="geetest-wrap"]/ul/li[5]/a[1]'

    user1 = "淡い柠檬草"
    pw1 = "56749154bB"

    def login_click(self):
        self.click(self.login)

    def user_name_type(self, text):
        self.type(self.username, text)
    
    def user_password_type(self, text):
        self.type(self.password, text)

    def login_btn_click(self):
        self.click(self.login_btn)
    
 
    # def send_submit_btn(self):
    #     self.click(self.research_btn)
    #     time.sleep(5)

    # def get_result(self):
    #     self.click(self.search_btn)