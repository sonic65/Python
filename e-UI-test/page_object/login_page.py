#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element

login = Element('login')

class LoginPage(WebPage):
    "登录类"
    def account_login(self, content):
        "账号登录"
        self.click_login_button

    def input_password(self, content):
        "输入密码"
        self.input_text(login['password'], txt=content)
        sleep()

    def input_username(self, content):
        "输入密码"
        self.input_text(login['username'], txt=content)
        sleep()

    def click_login_button(self):
        self.is_click(login['login_button'])
        sleep()
        
    def input_verify_code(self):
        """input verify code"""
        self.capture_element(login['验证码'])
        txt = self.capture_OCR()
        self.input_text(login['验证码输入'], txt)


if __name__ == '__main__':
    pass

