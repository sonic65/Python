import sys
print(sys.path)
print(sys.path.append('E:\Work\Project\Python\DEMO\sys\path.py'))

import sys
print(sys.path)
import os
os.chdir('/A／B／C')
for file in os.listdir(os.getcwd()):
     print(file)
sys.path.append('/A／B／C')
from C.XX import D