import pytest

from introduction import add

@pytest.mark.parametrize("a, b, result", [(2, 3, 5), (0, 0, 0), (-1, -1, -2)])
def test_add(a, b, result):
    assert add(a, b) == result