"""
test for nsarray_util
"""
from gcoreutils.detail.nsarray_util import (
    text_to_sympy_array,
    list_to_text,
    list_to_str,
    list_to_latex,
    bond_to_vector_center,
    bond_to_tail_head,
    bond_to_start_vector,
)


# ==================================================
def test_text_to_sympy_plus():
    data = [
        "",  # null
        "a",  # scalar
        "{a,b}",  # scalar (list)
        "{{a,b},{c,d}}",  # scalar (list)
        "[1,2,x]",  # vector
        "{[1,2,x]}",  # vector (1 list)
        "{[1,2,3],[4,5,6]}",  # vector (list)
        "[[1,2],[3,4]]",  # matrix
        "{[[1,2],[3,4]]}",  # matrix (1 list)
        "{[[1,2],[3,4]],[[5,6I],[7x,8y]]}",  # matrix (list)
        "[a,b]@[c,d]",  # bond
        "{[a,b]@[c,d]}",  # bond (1 list)
        "{[a,b]@[c,d],[1,2]@[3,4]}",  # bond (list)
        "[a,b];[c,d]",  # bond_th
        "{[a,b];[c,d]}",  # bond_th (1 list)
        "{[a,b];[c,d],[1,2];[3,4]}",  # bond_th (list)
        "[a,b]:[c,d]",  # bond_sv
        "{[a,b]:[c,d]}",  # bond_sv (1 list)
        "{[a,b]:[c,d],[1,2]:[3,4]}",  # bond_sv (list)
    ]

    for t in data:
        s, style, is_list, is_real = text_to_sympy_array(t)
        print(t, "=>", list_to_text(s, style, is_list), "| style =", style, "| is_list =", is_list, "| is_real =", is_real)
        print("  str  :", list_to_str(s, style, is_list))
        print("  latex:", list_to_latex(s, style, is_list))


# ==================================================
def test_bond_conversion():
    data = [
        "[a,b]@[c,d]",  # bond
        "{[a,b]@[c,d]}",  # bond (1 list)
        "{[a,b]@[c,d],[1,2]@[3,4]}",  # bond (list)
    ]

    for t in data:
        bond = text_to_sympy_array(t)[0]
        vc = bond_to_vector_center(bond, "bond")
        th = bond_to_tail_head(bond, "bond")
        sv = bond_to_start_vector(bond, "bond")
        print(bond.tolist(), "=> vector_center:", vc[0].tolist(), vc[1].tolist())
        print(bond.tolist(), "=> tail_head:", th[0].tolist(), th[1].tolist())
        print(bond.tolist(), "=> start_vector:", sv[0].tolist(), sv[1].tolist())


# ================================================== main
test_text_to_sympy_plus()
test_bond_conversion()
