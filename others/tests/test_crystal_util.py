"""
test for crystal_util
"""
from gcoreutils.crystal_util import cell_transform_matrix


# ==================================================
def test_crystal_util():
    cell_dict = {"c": 1.2}
    info = cell_transform_matrix(cell=cell_dict, crystal="hexagonal", translation=False)
    cell, volume, A, G, A_norm = info
    print("cell =", cell)
    print("volume =", volume)
    print("A =", A)
    print("G =", G)
    print("{a1, a2, a3} =", A_norm)


# ================================================== main
test_crystal_util()
