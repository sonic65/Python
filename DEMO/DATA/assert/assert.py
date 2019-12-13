import unittest

class TestCount(unittest.TestCase):
    def setUp(self):
       self.number=10

    def tearDown(self):
       pass
    '''
    断言括号内内容：实际值，期望值，提示信息
    '''

    #断言相等，若不相等，则用例失败，停止运行
    def test_assertEqual(self):
        print("请输入一个数字，验证与10相等")
        temp = int(input())
        self.assertEqual(temp,self.number,"数字不相等")

    #断言不相等，若相等，则用例失败，停止运行
    def test_assertNotEqual(self):
        print("请输入一个数字，验证与10不相等")
        temp = int(input())
        self.assertNotEqual(self.temp,self.number,"数字相等")

    #断言验证ture，为false则停止运行
    def test_true(self):
        self.assertTrue(3+5==9,"相加不相等，结果为假")

    # 断言验证false，为true则停止运行
    def test_false(self):
        self.assertFalse(3+5==8,"相加相等，结果为真")

    #验证a在b中，若不在，则停止运行
    def test_in(self):
        str1="I am a student"
        str2="dm"
        str3="am"
        self.assertIn(str2,str1,msg=(str2,"不在",str1,"中"))
        self.assertNotIn(str3,str1,msg=(str3,"在",str1,"中"))
    #验证a不在b中，若在，则停止运行
    def test_in(self):
        str1="I am a student"
        str3="am"
        self.assertNotIn(str3,str1,msg=(str3,"在",str1,"中"))

    #验证是同一个对象，若不是，则停止运行
    def test_is(self):
        str1="8"
        str2=8
        self.assertIs(str1,str2,"二者不是同一对象")
        #self.assertIsNot()不再赘述

    #验证是为空,若不为空，则停止运行
    def test_none(self):
        str="lalala"
        self.assertIsNone(str,msg=(str,"不为空"))
        #验证不为空不再赘述


if __name__=="__main__":
    unittest.main()