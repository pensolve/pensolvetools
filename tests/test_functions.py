from pensolvetools import functions as fn
import numpy as np


def test_sanity():
    assert 1 == 1


def test_concat():
    assert fn.concat(['a', 4, 't']) == 'a4t'
    a = np.array([1500, 1200])
    b = np.array([1400, 1500])
    vals = fn.concat([a, '-', b])
    assert vals[0] == '1500-1400', vals


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


def test_p_min():
    vals = fn.p_min([4, [5, 3], 2])
    assert vals[0] == 2
    assert vals[1] == 2
    assert fn.p_min([5, 'cow', 3]) == 3
    assert fn.p_min([5, np.array(4), 8]) == 4

def test_p_max():
    vals = fn.p_max([4, [5, 3], 2])
    assert vals[0] == 5
    assert vals[1] == 4
    assert fn.p_max([5, 'cow', 3]) == 5
    assert fn.p_max([5, np.array(8), 3]) == 8


def test_p_sum():
    assert fn.p_sum([4, [5, 3], 2]) == 14
    assert fn.p_sum([5, 'cow', 3]) == 8
    assert fn.p_sum([5, np.array(4), 8]) == 17



if __name__ == '__main__':
    test_concat()

