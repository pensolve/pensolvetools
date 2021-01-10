from pensolvetools import functions as fn

def test_sanity():
    assert 1 == 1


def test_concat():
    assert fn.concat(['a', 4, 't']) == 'a4t'


if __name__ == '__main__':
    test_concat()

