base on PyTest

refer:

https://www.jianshu.com/p/932a4d9f78f8
https://www.jianshu.com/p/e31c54bf15ee
https://www.cnblogs.com/zhangshan33/p/11940356.html
https://github.com/zhangshan33/ATScripts


Request.py 封装request方法，可以支持多协议扩展（get\post\put）
Config.py读取配置文件，包括：不同环境的配置，email相关配置
Log.py 封装记录log方法，分为：debug、info、warning、error、critical
Email.py 封装smtplib方法，运行结果发送邮件通知
Assert.py 封装assert方法
run.py 核心代码。定义并执行用例集，生成报告

手动生成报告：
Pytest：
allure generate report/result -o report/allure_html --clean