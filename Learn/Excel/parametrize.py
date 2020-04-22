import pytest
import sys

sys.path.append('/Users/sonic/Project/Python/Pytest/settings')
import conf

from ExcelHandler import ExcelHandler
import xlrd

'''
# 单参数
@pytest.mark.parametrize('name1', ['sunny'])
def test_name1(name1):
    print('+++', name1)
    assert name1 == 'sunny'


# 多参数
@pytest.mark.parametrize('name', ['sunny', 'kevinse', 'jacky'])
def test_name2(name):
    print('---', name)
    assert 'sunny' in name


多参数
name = 'sunny'
@pytest.mark.parametrize('name', ['sunny', 'kevinse', 'jacky'])
def test_name3(name):
    print('@@@', name)
    assert name == 'sunny'


# 多参数 多值
@pytest.mark.parametrize('name, pwd', [('sunny', 111), ('kevinse', 222), ('jacky', 333)])
def test_name3(name, pwd):
    print('@@@', name, pwd)


#组合
@pytest.mark.parametrize('x', [1, 2])
@pytest.mark.parametrize('y', [3, 4])
def test_name4(x, y):
    print('组合', x, y)
'''

#Excel
@pytest.mark.parametrize('data', ExcelHandler().get_excel_data)
def test_excel(data):
    # assert data == '<Response [200]>'
    print(data)
