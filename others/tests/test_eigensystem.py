"""
test for eigensystem
"""
import numpy as np
from gcoreutils.eigensystem import eigensystem


# ==================================================
def mat_func(params):
    """
    a function to create a set of hermitian matrix.

    Args:
        params (np.array): a set of parameters in each row

    Returns:
        list: hermitian matrix, in which each element is a set of parameters (1d np.array)
    """
    e1, e2, v = params.T  # do not forget transpose
    mat = [[e1, np.sin(v)], [np.sin(v), e2]]  # a hermitian matrix by parameters
    return mat


# ==================================================
def test_eigensystem():
    print("=== eigensystem ===")
    params = np.array([[1, 2, 0.0], [1, 2, 0.1], [1, 2, 0.2], [1, 2, 0.3], [1, 2, 0.4], [1, 2, 0.5]])
    vals, vecs = eigensystem(mat_func, params)
    print("--- eigen values ---")
    print(vals)
    print("--- eigen vectors ---")
    print(vecs)


# ================================================== main
test_eigensystem()
