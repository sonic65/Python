#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element

login = Element('login')

class LoginPage(WebPage):
    "登录类"
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


if __name__ == '__main__':
    pass

