#匹配
#re.match(pattern, string, flags=0)
'''
参数	描述
pattern	匹配的正则表达式
string	要匹配的字符串。
flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
'''

import re

print(re.match('www', 'www.runoob.com').span())
print(re.match('com', 'www.runoob.com'))