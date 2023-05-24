"""
test for basic_util
"""
from gcoreutils.basic_util import apply, get_variable, set_variable
import sympy as sp


# ==================================================
def test_apply():
    data = [1, [1, 2], [[1, 2], [3], 4], [1, [[2, 3], 4]]]

    for d in data:
        s = apply(lambda i: str(i), d)
        print(d, "=>", s)


# ==================================================
def test_get_set_variable():
    data = ["x", "a * b * c", "sqrt(3*x+I+y+3)"]

    lst = []
    for d in data:
        s = sp.sympify(d)
        lst.append(s)
        v = get_variable(s)
        print(d, "=>", v)

    v = get_variable(lst)
    print(lst, "=>", v)
    print(set_variable(v, real=True))


# ================================================== main
test_apply()
test_get_set_variable()
