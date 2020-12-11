import os

 def testCase(platformName,platformVersion,deviceName,app,appPackage,appActivity,port):

    PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
    capabilities = {}
    capabilities['platformName'] = 'Android' #设置平台
    capabilities['platformVersion'] = '4.1' #系统版本
    capabilities['deviceName'] = '127.0.0.1:62001' #设备id
    capabilities['autoLaunch'] = 'true' #是否自动启动
    capabilities['app'] = PATH('../apps/mukewang.apk' )#安装包路径，放在该py文件的目录下)
    capabilities['appPackage'] = 'cn.com.open.mooc' #包名
    capabilities['appActivity'] = 'cn.com.open.mooc.aindex.splash.MCSplashActivity' #启动的activity
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)