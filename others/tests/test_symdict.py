"""
test for symdict
"""
import sympy
from gcoreutils.symdict import SymDict


# ==================================================
def test_symdict():
    print("=== symdict ===")
    t1 = sympy.symbols("t_1", real=True)
    t2 = sympy.symbols("t_2", real=True)
    Delta = sympy.symbols("Delta", real=True)
    lam = sympy.symbols("lambda", real=True)

    d1 = SymDict({"1": t1, "2": Delta, "3": lam})
    d2 = SymDict({"2": 2 * t2, "3": Delta, "4": lam, "5": 0})

    v = sympy.sqrt(3)

    print("before =", d1, d2)
    print(d1 + d2)
    print(d1 - d2)
    print(d1 * d2)
    # print(d1 / d2)
    print(d1 / v)
    print(v / d1)
    print(d1 + v)
    print(d1**v)
    print("after  =", d1, d2)
    d1 += d2
    d1.simplify()
    print(d1)
    d1.remove_zero()
    print(d1)


# ================================================== main
test_symdict()
