from introduction import add

def test_add():
    assert add(2, 5) == 7
    assert add(0, 0) == 0
    assert add(0, -1) == -1
    assert add(-1, -1) == -2