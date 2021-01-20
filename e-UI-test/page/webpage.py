#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from config.conf import LOCATE_MODE
from tools.times import sleep
from tools.logger import log

"""
selenium基类
本文件存放了selenium基类的封装方法
"""

class WebPage(object):
    """selenium基类"""

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.timeout = 20
        self.wait = WebDriverWait(self.driver, self.timeout)

    def get_url(self, url):
        """打开网址并验证"""
        # self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            log.info("打开网页：%s" % url)
        except TimeoutException:
            raise TimeoutException("打开%s超时请检查网络或网址服务器" % url)

    @staticmethod
    def element_locator(func, locator):
        """元素定位器"""
        name, value = locator
        return func(LOCATE_MODE[name], value)

    def find_element(self, locator):
        """寻找单个元素"""
        return WebPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_element_located(args)), locator)

    def find_elements(self, locator):
        """查找多个相同的元素"""
        return WebPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_all_elements_located(args)), locator)

    def elements_num(self, locator):
        """获取相同元素的个数"""
        number = len(self.find_elements(locator))
        log.info("相同元素：{}".format((locator, number)))
        return number

    def input_text(self, locator, txt):
        """输入(输入前先清空)"""
        sleep(0.5)
        ele = self.find_element(locator)
        ele.clear()
        ele.send_keys(txt)
        log.info("输入文本：{}".format(txt))

    def is_click(self, locator):
        """点击"""
        self.find_element(locator).click()
        sleep()
        log.info("点击元素：{}".format(locator))

    def element_text(self, locator):
        """获取当前的text"""
        _text = self.find_element(locator).text
        log.info("获取文本：{}".format(_text))
        return _text

    @property
    def get_source(self):
        """获取页面源代码"""
        return self.driver.page_source

    def refresh(self):
        """刷新页面F5"""
        self.driver.refresh()
        self.driver.implicitly_wait(30)

    def capture_element(self, locator):
        """元素截图"""
        self.find_element(locator).screenshot(r'./screen_capture/capture_code.png')
        log.info("Capture element to /page_object/")

    def switch_to_alert(self):
        self.driver.switch_to_default_content() 

    # def wait_for_element(self, content):
    #     WebDriverWait(self.driver,10,1).until(EC.visibility_of_element_located((By.ID,content)))

    def send_keys_Space(self):
        """按键"""
        log.info("按键")
        self.driver.send_keys(Keys.SPACE)

    def forward(self):
        """浏览器前进操作"""
        self.driver.forward()
        log.info("Click forward on current page.")

    def back(self):
        """浏览器后退操作"""
        self.driver.back()
        log.info("Click back on current page.")

    def wait(self, seconds):
        """浏览器等待"""
        self.driver.implicitly_wait(seconds)
        log.info("wait for %d seconds." % seconds)

    def move_to_element(self, contentA, contentB):
        self.driver.ActionChains(self.driver).move_to_element(contentA).click(contentB).perform()

    def capture_element(self, locator):
        """元素截图"""
        self.find_element(locator).screenshot(r'./screen_capture/capture_code.png')
        log.info("Capture element to /page_object/")

    def capture_OCR(self):
        from tools.baidu_aip import identify_words 
        r = identify_words()
        return r

if __name__ == "__main__":
    pass
