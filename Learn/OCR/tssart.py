# coding = utf-8
from selenium import webdriver
import time
import json
import numpy as np
import pytesseract
import datetime
import os
from PIL import Image, ImageEnhance

import sys
sys.path.append("./")

from util.Log import Logger

file_name = os.path.split(__file__)[-1].split(".")[0]
logger = Logger(logger = file_name).getLog()


def recognition_image(driver, lang, className, pageName):
    driver.save_screenshot('./data/image.png')
    codeEelement = driver.find_element_by_class_name(className)
    
    logger.debug('开始识别', pageName)
    logger.debug('图片', codeEelement, type(codeEelement))
    imgSize = codeEelement.size  # 获取图片的大小

    logger.debug('图片大小', imgSize, type(imgSize))
    imgLocation = codeEelement.location  # 获取元素坐标
    logger.debug('图片位置', imgLocation, type(imgLocation))
    rangle = (int(imgLocation['x']), int(imgLocation['y']), int(imgLocation['x'] + imgSize['width']),int(imgLocation['y'] + imgSize['height']))  # 计算验证码整体坐标
    image = Image.open(r'code.png').convert('RGB')

    imageImg = image.crop(rangle)  # 截取验证码图片
    imageImg = imageImg.convert("L")#convert()方法传入参数L，将图片转化为灰度图像
    text = pytesseract.image_to_string(imageImg, lang)

    return text

if __name__ == "__main__":
    recognition_image()