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

## WebDriverAgent
git clone https://github.com/appium/WebDriverAgent.git

 - cd WebDriverAgent
 - mkdir -p Resources/WebDriverAgent.bundle
 - sh ./Scripts/bootstrap.sh
  修改Product Bundle Identifier为唯一  如：com.sonic.WebDriverAgentLib

安装Agent https://blog.csdn.net/qq_41030861/article/details/110528139

> 常见错误：
1.'RoutingHTTPServer/RoutingConnection.h' file not found while building webDriverAgent project in Xcode
到WebDriverAgent的根目录下 执行 bash Scripts/bootstrap.sh -d
2.WebDriverAgent.bundle: No such file or directory
到WebDriverAgent的根目录下 执行./Scripts/bootstrap.sh（作用：安装依赖库，同时使用npm 打包响应的js 文件）


# Android SDK Tools
https://www.cnblogs.com/nebie/p/9145627.html
https://www.androiddevtools.cn/

# sample-code 
https://github.com/appium/appium.git