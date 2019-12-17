# coding=utf-8
from common.base_page import BasePage
 
 
class HomePage(BasePage):
 
    input_box = "id=>kw"
    search_submit_btn = "xpath=>//*[@id='su']" 
    search_btn = "xpath=>/html/body"
    search_result_string ="xpath=>//*/div[@class='nums']"
    new_string = '约'
    last_result = '个'

 
    def type_search(self, text):
        self.type(self.input_box, text)
 
    def send_submit_btn(self):
        self.click(self.search_btn)

    def send_submit_btn(self):
        self.click(self.search_btn)