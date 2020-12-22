# 启动参数
​
app.run(debug=True, threaded=True, port=5000, host=‘0.0.0.0’)
debug | 是否开启调试模式，默认为False；开启后会自动加载代码
threaded | 是否开启多线程，默认是不开启的
port | 指定端口号
host | 指定主机，设置为’0.0.0.0’之后可以通过IP访问