#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import json
import time
import requests


class Passport:

    __janus_url = 'http://baidu.com'

    def __init__(self, eid, epw):
        self.ele_id = eid
        self.ele_pw = epw
        self.janus = {}
        self.ticket = {}
        self.accessToken = {}
        self.accessId = {}
        self.getJanusToken()
        self.ssoToken = self.getSsoToken()
        self.init_app_passport()

    def init_app_passport(self):
        self.getAppAccess('ba2465da-bf8b-4c32-9b42-78eeb76954c7', '百度')

    def getJanusToken(self):
        h = {"Content-Type": "application/json;charset=UTF-8"}
        p = {"clientType": 1,
             "identity": self.ele_id,
             "password": self.ele_pw,
             "code": "",
             "thirdAppKey": "",
             "timestamp": int(time.time() * 1000)}
        try:
            r = requests.post(
                url=self.__janus_url+'/api/v1/auth/sms/login',
                data=json.dumps(p),
                headers=h)
            if r.status_code == 200:
                res = json.loads(r.content)
            if res["code"] == 0:
                data = res["data"]
                self.janus["authToken"] = data["authToken"]
                self.janus["sessionId"] = data["sessionId"]
        except Exception as e:
            raise e

    def getAppTicket(self, appkey):
        ticket = ""
        if not self.janus:
            self.getJanusToken()
        h = {"Content-Type": "application/json;charset=UTF-8", "auth-token": self.janus["authToken"]}
        p = {"thirdAppKey": appkey}
        try:
            r = requests.post(
                url=self.__janus_url+'/api/v1/sessions/%s/tickets' % self.janus["sessionId"],
                data=json.dumps(p),
                headers=h)
            if r.status_code == 200:
                res = json.loads(r.content)
            if res["code"] == 0:
                data = res["data"]
                self.ticket[appkey] = data["ticket"]
                ticket = data["ticket"]
        except Exception as e:
            raise e
        return ticket

    def getAppAccess(self, appkey, appauthurl):
        h = {"Content-Type": "application/json;charset=UTF-8"}
        try:
            if appkey not in self.ticket.keys():
                self.getAppTicket(appkey)
                p = {"sessionId": self.janus['sessionId'], "ticket": self.ticket[appkey]}
            r = requests.post(
                url=appauthurl,
                data=json.dumps(p),
                headers=h)
            if r.status_code == 200:
                res = json.loads(r.content)
            if res["code"] == 0:
                data = res["data"]
                self.accessToken[appkey] = data["accessToken"]
                self.accessId[appkey] = data["accessId"]
        except Exception as e:
            raise e

    def getSsoToken(self):
        ssoToken = ""
        if not self.janus:
            return
        h = {"auth-token": self.janus["authToken"], "Content-Type": "application/json;charset=UTF-8"}
        try:
            r = requests.post(
                url=self.__janus_url + "/api/v1/sessions/%s/ssoToken" % self.janus["sessionId"],
                headers=h)
            if r.status_code == 200:
                res = json.loads(r.content)
                ssoToken = res['data']
                self.ssoToken = res['data']
        except Exception as e:
            raise e
        return ssoToken

if __name__ == "__main__":
    inToken =Passport('E060086', '1').ssoToken
    print(inToken)