import pytest
import sys
sys.path.append('/Users/sonic/Project/Python/Pytest/settings')
import conf
import sys
sys.path.append('/Users/sonic/Project/Python/Pytest')
from excel import ExcelHandler
import xlrd

@pytest.mark.parametrize('name', ['sunny', 'kevinse', 'jacky'])
def test_name(name):
    print('---',name)

@pytest.mark.parametrize('data', ExcelHandler.get_excel_data(1))
def test_excel(data):
    assert data == '<Response [200]>'
    print('**',data)