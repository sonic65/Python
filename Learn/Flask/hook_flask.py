# coding:utf-8
# referer: https://blog.csdn.net/houyanhua1/article/details/85342281
 
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello Flask"
 
@app.route("/index")
# 视图函数
def index():
    print("index 被执行")
    a = 1 / 0   # 在视图函数中，手动抛出异常
    return "index page"
 
@app.before_first_request
def handle_before_first_request():
    """在第一次请求处理之前被执行 (服务器启动后,只会执行一次)"""
    print("handle_before_first_request 被执行")
 
@app.before_request
def handle_before_request():
    """在每次请求之前都被执行"""
    print("handle_before_request 被执行")
 
@app.after_request
# 必须传入response参数(视图函数返回的response)
def handle_after_request(response):
    """在每次请求(视图函数处理)之后都被执行, 前提是视图函数没有出现异常"""
    print("handle_after_request 被执行")
    return response   # 一般返回response，表示放行 
 
@app.teardown_request
# 必须传入response参数(视图函数返回的response)
def handle_teardown_request(response):
    """在每次请求(视图函数处理)之后都被执行，无论视图函数是否出现异常都被执行(只有在生产环境下才会执行)"""
    print("handle_teardown_request 被执行")
    return response  # 一般返回response，表示放行
 
if __name__ == '__main__':
    app.run(debug=True)  # 以生产环境方式启动服务器
 
# handle_before_first_request 被执行
# handle_before_request 被执行
# index 被执行
# handle_after_request 被执行
# handle_teardown_request 被执行