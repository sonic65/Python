from classA import ClassA

class ClassB(ClassA):

    def test_inherit(self):
        self.open_baidu()

test=ClassB()
test.test_inherit()