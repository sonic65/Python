#使用import
import unittest

#测试用例TestCase
'''
一个测试用例时一个完整的测试流程，包括了环境准备SetUp，测试执行Run，测试环境还原TearDown
一个测试用例时一个完整的测试单元，验证一个功能是否正确
'''
class test_case(unittest.TestCase):
    #setUp和tesrDown方法，可以为每一个测试方法所复用，即每运行一个测试用例，都是在运行前后分别调用一下两个方法
    def setUp(self):
        #存放初始化的内容
        #浏览器的启动，url地址，连接数据库，设置全局等待······
        pass
    def tearDown(self):
        #无论用例通过与否，在测试用例结束后都会调用这个方法，处理善后工作，如关闭浏览器等
        pass
    def test_balabala1(self):
        #验证功能A的第1个测试用例
        # 测试用例要以"test_"开头，否则编译器将其作为一个测试方法来运行
        pass
    def test_balabala2(self):
        #验证功能A的第2个测试用例
        pass


#全局的main方法，使用这条语句语句可以将一个单元测试模块编程直接可以执行的脚本
if __name__=="__main__":
    #不构造测试集，直接测试
    # unittest.main()

    #构造测试集
    suite=unittest.TestSuite()
    suite.addTest(test_case("test_balabala1"))
    suite.addTest(test_case("test_balabala2"))

    #执行测试
    '''
    TextTestRunner用于执行测试用例，可以使testcase，也可以是testsuite
    测试的结果保存在TestResult中，包括执行了、通过了、失败了的用例信息
    '''
    runner=unittest.TextTestRunner()
    runner.run(suite)