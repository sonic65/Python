import allure
import pytest
from ExcelHandler import ExcelHandler


@pytest.mark.parametrize('case', ExcelHandler().get_excel_data)
def test_case(case):
    """  执行断言 """
    print('case:',case)
