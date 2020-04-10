# coding=utf-8
import time
from selenium import webdriver
 
 
class HomePage():
 
    input_box = 'xpath=>//*[@id="sb_form_q"]'
    search_submit_btn = 'class=>b_searchboxSubmit]'
    search_class = 'xpath=>/html/body/table/tbody/tr/td/div/div[2]/div[3]/form/div/div[1]/input'
    search_result_string ="class=>sb_count"
    research_btn = "id=>sb_go_par"
    new_string = '条'
    est_en = "id=>est_en"
    text1 = 'selenium'
    text2 = 'python'
 
    def search_btn(self):
        driver = webdriver.Chrome()
        driver.get('http://bing.com')
        time.sleep(5)

        driver.find_element_by_xpath('//*[@id="sb_form_q"]').send_keys("333")
        time.sleep(2)
        c = driver.find_element_by_xpath('//*[@id="sb_form_go"]')
        c.click()
        time.sleep(1)

        driver.quit()


    # def get_result(self):
    # self.click(self.search_btn)

t = HomePage()
t.search_btn()

# if __name__ == "__main__":
#     pass