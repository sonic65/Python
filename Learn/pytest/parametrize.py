def add(x, y):
    return x + y

import pytest

@pytest.mark.parametrize(
    "x, y , expect",
    [
        (1, 2, 3),
        (10, 10, 20),
        (200, 3000, 4000),
    ]
)

def test_add(x, y, expect):
    """
    docstring
    """
    assert add(x, y) == expect
