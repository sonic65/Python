from selenium import webdriver
import configparser
import os

import sys   
sys.path.append('/Users/sonic/Project/Python/MyFrame/common')
from common.logger import Logger
import time
from selenium import webdriver


config = configparser.ConfigParser()
config_path = os.path.dirname(os.path.abspath('.')) + '/MyFrame/common/config.ini'
print(config_path)

screen_path = os.path.dirname(os.path.abspath('.')) + '/MyFrame/screenshots/'

rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
screen_name = screen_path + rq + '.png'

print(screen_path)
print(screen_name)

driver = webdriver.Chrome()
driver.get_screenshot_as_file(screen_name)
    