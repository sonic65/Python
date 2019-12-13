import time
from selenium import webdriver 

#以utf-8的编码、只读的形式打开文件
data=open("./data.txt","r",encoding="utf-8")
#读取每一行的数据内容
values=data.readlines()
#读取完成后关闭文件
data.close()
#遍历读取到的内容，将每次遍历的结果使用百度搜索
for value in values:
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    driver.find_element_by_id("kw").send_keys(value)
    driver.find_element_by_id("su").click()
    time.sleep(3)
    driver.quit()
    print(value)
