from functions import encryption

def test_encryption():
    assert encryption('hello') == 'Encoded Message:	ãäïóú'

def test_add():
    assert add(1 3) == 4