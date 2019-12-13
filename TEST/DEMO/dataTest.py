import A
import unittest

#参数化数字
class Data(object):
    def __init__(self,x='',y='',z=''):
        self.x=x
        self.y=y
        self.z=z

s1=Data(x=1,y=2,z=3)
s2=Data(x=1,y=2,z=-1)
#参数化数字 通过u1.x,u1.y引用

#unittest模块
class TestCount(unittest.TestCase):
    def setUp(self):
       self.number=10
    def tearDown(self):
       pass

    def test_add(self):
        print("验证A.add")
        m = A.add(s1.x,s1.y) #引用data
        print(m)
        self.assertEqual(s1.z,m,"1+2=3 Right")
        #断言括号内内容：实际值，期望值，提示信息

    def test_sub(self):
        print("验证A.sub")
        self.assertEqual(s2.z,A.sub((s2.x),(s2.y)),"1-2=-1 Right")
    
    def test_mul(self):    
        print("验证A.mul")
        self.assertEqual(2,A.mul(1,2),"1*2=2 Right")

    def test_div(self):        
        print("验证A.div")
        self.assertEqual(0.5,A.div(1,2),"1/2=0.5 Right")

if __name__=="__main__":
    unittest.main()
