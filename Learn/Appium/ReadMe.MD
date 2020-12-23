# Infrustructure
Node.js
JDK
Python
X-Code


# appium安装，有两种方式。
1、客户端安装
https://github.com/appium/appium-desktop/releases/tag/v1.15.1

2、命令行安装
npm install -g appium
npm --registry https://registry.npm.taobao.org/ install -g appium

# Appium-Python-Client （done）
sudo pip install Appium-Python-Client
sudo cnpm install -g appium-doctor


# IOS 真机
referer:https://blog.csdn.net/weixin_43291944/article/details/103562488

brew install libimobiledevice --HEAD
npm install -g ios-deploy  
brew install carthage
   - 查看模拟器列表：instruments -s devices
   - 查看真机列表：idevice_id -l
   - 安装App：ideviceinstaller -i demo.app

## webdriverAgent
git clone https://github.com/facebook/WebDriverAgent
cd WebDriverAgent
sh ./Scripts/bootstrap.sh
安装Agent https://www.cnblogs.com/meitian/p/7359787.html

# Android SDK Tools
https://www.cnblogs.com/nebie/p/9145627.html
https://www.androiddevtools.cn/

# sample-code 
https://github.com/appium/appium.git