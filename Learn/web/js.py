from selenium import webdriver
import time
#pip3 install PyExecJS
import execjs
#打开百度
# driver=webdriver.Chrome()


# js1 = "javascript:alert((function() {     var date = new Date()   ;  var str = `${(date.getMonth() + 1).toString().padStart(2, '0')}${date.getDate().toString().padStart(2, '0')}`    ; return str.split('').map(char => {         return (+char + date.getDay()) % 10     }).join('') })())"
# result = driver.execute_script(js1)
# print(result)


script = open("/Users/gaoyuhang/Project/Python/Learn/web/code.js", "r")
script_content = script.read()
script.close()
x = execjs.compile(script_content)
print(x)

