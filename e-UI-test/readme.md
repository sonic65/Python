# web-UI 自动化测试示例
https://blog.csdn.net/oHuaXin1234/article/details/107115030?utm_medium=distribute.pc_relevant.none-task-blog-title-6&spm=1001.2101.3001.4242

---

## 框架设计

- pytest
- selenium
- POM 模型

---

## 目录结构

    common                 ——公共类
    Page                   ——基类
    PageElements           ——页面元素类
    PageObject             ——页面对象类
    TestCase               ——测试用例
    conf.py                ——各种固定配置
    conftest.py            ——pytest胶水文件
    pytest.ini             ——pytest配置文件

---

## 运行

- `cd 项目目录`

* MacOS 系统或 Linux 系统

- 在命令行输入`sh run_mac.sh`即可运行

* Windows 系统

- 在命令行输入`run_mac.bat`即可运行


# allure参数说明


- allure --alluredir
- allure generate
    - -c 生成报告前删除上一次生成的报告
    - -o 指定生成的报告目录
- allure open --alluredir

# app_autotest_v

- 执行：pytest
- 生成allure格式结果：//pytest -s -q --alluredir report
    - pytest --alluredir report/result

- 生成allure报告： //allure generate directory-with-results/ -o directory-with-report
    - allure generate report/result -o report/allure_html --clean


# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "1641839697@qq.com"  # 用户名
# mail_pass = "ygarpyvxlllgcbcc"  # 口令

# 元素定位的类型
LOCATE_MODE = {
    'css': By.CSS_SELECTOR,
    'xpath': By.XPATH,
    'name': By.NAME,
    'id': By.ID,
    'class': By.CLASS_NAME
}