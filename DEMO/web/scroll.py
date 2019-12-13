from selenium import webdriver
import time
#打开百度
driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
#搜索selenium，制造含有滚动条的环境
kw=driver.find_element_by_id("kw")
kw.send_keys("selenium")
su=driver.find_element_by_id("su")
su.click()
time.sleep(2)

#拖动滚动条至底部
js1="document.documentElement.scrollTop=10000"
driver.execute_script(js1)
time.sleep(3)

#拖动滚动条至顶部
js2="document.documentElement.scrollTop=0"
driver.execute_script(js2)
time.sleep(3)

driver.quit()

'''
#左右方向的滚动条可以使用window.scrollTo(左边距，上边距)方法
#example
js="window.scrollTo(200,1000)"
driver.execute_script(js)
'''