from pensolvetools import functions as fn
import numpy as np


def test_sanity():
    assert 1 == 1


def test_concat():
    assert fn.concat(['a', 4, 't']) == 'a4t'


def test_match_case0():
    x = ['Height', 'TC1', 'TC 1.5', 'TC2', 'TC 2.5', 'TC3', 'TC4']
    x0 = 'TC1'
    ind = fn.match(x0, x, 0)
    assert ind == 1
    a = np.where(x0 == np.array(x))[0][0].item()
    print(a)


def test_match_case1():
    x = np.arange(1, 5)
    x0 = 1
    ind = fn.match(x0, x, 1)
    assert ind == 0, ind
    x0 = 1.2
    ind = fn.match(x0, x, 1)
    assert ind == 0, ind
    x0 = 2
    ind = fn.match(x0, x, 1)
    assert ind == 1, ind


def test_match_case_neg1():
    x = np.arange(1, 5)[::-1]
    x0 = 1.2
    ind = fn.match(x0, x, -1)
    assert ind == 3, ind
    x0 = 1
    ind = fn.match(x0, x, -1)
    assert ind == 4, (ind, f'x0={x0}')
    x0 = 2
    ind = fn.match(x0, x, -1)
    assert ind == 3, ind

if __name__ == '__main__':
    test_match_case_neg1()

