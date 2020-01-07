from selenium import webdriver
import configparser
import os

import sys   
sys.path.append('/Users/sonic/Project/Python/MyFrame/common')
from common.logger import Logger


logger = Logger(logger="").getlog()

class BrowserEngine(object):

    # dir = os.path.dirname(os.path.abspath('.'))  # 注意相对路径获取方法
    # chrome_driver_path = dir + '/tools/chromedriver.exe'
    # ie_driver_path = dir + '/tools/IEDriverServer.exe'

    def __init__(self,driver):
        self.driver = driver

    browser_type = ""   
    # browser_type = "IE"    
    # browser_type = "Firefox"     

    def open_browser(self,driver):

        config = configparser.ConfigParser()
<<<<<<< HEAD
        config_path = os.path.dirname(os.path.abspath('.')) + 'common/config.ini'
=======
        config_path = os.path.dirname(os.path.abspath('.')) + '/MyFrame/common/config.ini'
>>>>>>> dd221c29427f8c75cd244a1ed35aaa9546d9319c
        config.read(config_path)
        browser_type = config.get("browserType","browserName")
        logger.info("you had select %s browser."% browser_type)
        url = config.get("testServer","URL")
        logger.info("The test URL is: %s" % url)

        if browser_type == 'Firefox':
            driver = webdriver.Firefox()
        elif browser_type == 'Chrome':
            driver = webdriver.Chrome()
        elif browser_type == 'IE':
            driver = webdriver.IE()
        else: driver = webdriver.Chrome()

        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()
