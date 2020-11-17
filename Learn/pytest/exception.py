import pytest

def fun(x):
    if x == 0:
        raise ValueError("x is 0 ")
    else:
        print('OK')

# fun(0)


def test_exception1():
    with pytest.raises(ValueError):
        fun(1)

def test_exception2():
    assert fun(0) == None