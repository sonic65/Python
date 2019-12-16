import time
from selenium import webdriver

class GetString(object):

    def get_search_result(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)

        driver.get('https://www.baidu.com')
        driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(5)
        driver.find_element_by_xpath('/html/body').click()
        time.sleep(5)

        search_result_string = driver.find_element_by_xpath("//*/div[@class='nums']").text
        print (search_result_string)

        new_string = search_result_string.split('约')[1]
        print (new_string)
        last_result = new_string.split('个')[0]
        print (last_result)


getstring = GetString()
getstring.get_search_result()