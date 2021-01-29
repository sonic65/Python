from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_css_selector('#kw').send_keys(123)
time.sleep(1)
driver.find_element_by_css_selector('#kw').clear()
url = driver.current_url
t = driver.title
print(t, url)