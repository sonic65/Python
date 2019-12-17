# coding=utf-8
from common.base_page import BasePage
import time
 
 
class HomePage(BasePage):
 
    input_box = 'xpath=>//*[@id="sb_form_q"]'
    search_submit_btn = 'class=>b_searchboxSubmit]'
    search_class = 'xpath=>/html/body/table/tbody/tr/td/div/div[2]/div[3]/form/div/div[1]/input'
    search_result_string ="class=>sb_count"
    research_btn = "id=>sb_go_par"
    new_string = '条'
    est_en = "id=>est_en"
    text1 = 'selenium'
    text2 = 'python'
 
    def type_search(self, text):
        self.type(self.input_box, text)

    def est_click(self):
        self.click(self.est_en)

    def type_clear(self):
        self.clear(self.input_box)
    
    def search_btn(self):
        self.click(self.search_class)
 
    def send_submit_btn(self):
        self.click(self.search_submit_btn)
        time.sleep(5)

    # def get_result(self):
    #     self.click(self.search_btn)