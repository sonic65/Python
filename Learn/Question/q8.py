

import sys 
#str = input()

import re

def phone():
    
    x = input('input a Phone: ')

    x1 = re.sub(r'#.*$', "", x)
    #print(str)
    x2 = re.sub(r'\D', "", x1)
    print(x1)
    print(x2)
phone()