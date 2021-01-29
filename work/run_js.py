# dyt 验证码
js = "function() {     var date = new Date()   ;  var str = `${(date.getMonth() + 1).toString().padStart(2, '0')}${date.getDate().toString().padStart(2, '0')}`    ; return str.split('').map(char => {         return (+char + date.getDay()) % 10     }).join('') }()"

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.execute_script(js)


import execjs

code = execjs.eval(js)
print(code)