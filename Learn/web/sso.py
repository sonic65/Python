# coding=utf-8
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time


def login():
    path = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(path)
    driver.get('https://sso.rajax-inc.com')
    # os.system(2)
    driver.find_element_by_class_name("tachyon-icon").click()
    driver.find_element_by_xpath('//*[@id="app"]/div/section/div/div/section/section/div/label[1]/input').send_keys(
        'E010785')
    driver.find_element_by_xpath('//*[@id="app"]/div/section/div/div/section/section/div/label[2]/input').send_keys(
        '123456')
    driver.find_element_by_xpath('//*[@id="app"]/div/section/div/div/section/section/div/div[2]/input').send_keys('1')
    driver.find_element_by_class_name('tachyon-classic__submit').click()
    time.sleep(5)
    driver.find_element_by_class_name('sso-header-search__input').send_keys("招聘管理4", Keys.ENTER)
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/section[1]/section/div[1]/section/div/section/div/h3').click()
    time.sleep(5)

    driver.switch_to.window(-1)


    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[1]/div/ul/li[2]/span/span").click()

    os.system(5)



if __name__ == '__main__':
    login()