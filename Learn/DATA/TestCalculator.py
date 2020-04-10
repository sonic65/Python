import Calculator
import unittest

class TestCount(unittest.TestCase):
    def setUp(self):
       self.number=1

    def tearDown(self):
       pass

    def test_add(self):
        print("验证A.add")
        self.assertEqual(3,Calculator.add(1,2),"1+2=3 Right")
        #断言括号内内容：实际值，期望值，提示信息

    def test_sub(self):
        print("验证A.sub")
        self.assertEqual(-12,Calculator.sub(1,2),"1-2=-1 Right")
    
    def test_mul(self):    
        print("验证A.mul")
        self.assertEqual(2,Calculator.mul(1,2),"1*2=2 Right")

    def test_div(self):        
        print("验证A.div")
        self.assertEqual(0.5,Calculator.div(1,2),"1/2=0.5 Right")


if __name__=="__main__":
    unittest.main()


'''
print(A.add(1,2))
assert(A.add(1,2) == 3)
'''