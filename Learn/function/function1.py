#提取数字

import re
import sys

def str():
    string = input("Input a String: " )
    print(string)
    str_number = re.sub('\D','',string)
    print(str_number)
    lenth = len(str_number)
    print(lenth)
    result = (int(str_number) // lenth)
    print(result)

#str()

if __name__ == '__main__':
    str()
