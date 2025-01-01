# app.py
# This is a test commit
# This commit is done by Subhash
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    assert add(10, 20) == 30
    assert add(50, 50) == 100
