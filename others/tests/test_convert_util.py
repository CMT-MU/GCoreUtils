"""
test for convert_util
"""
from gcoreutils.convert_util import (
    text_to_sympy,
    is_valid_sympy,
    text_to_list,
    sympy_to_str,
    sympy_to_float,
    sympy_to_complex,
    sympy_to_latex,
    sympy_to_mathematica,
)


# ==================================================
def test_convert_util():
    test = [
        "x+y",
        "[a,,1.3]",
        "[a,b,c, 2/3,sqrt(3)]",
        "[[sin(x),cos(y),3+x],[x y z,y z x,z x y]]",
        "[[ [sin(x),cos(y),3+x],[x,y,z] ], [1,I, y] ]",
        "[[ [sin(x),cos(y),3+x],[x,y,z] ], [1,I, y],a]",
        "[[ [sin(x),cos(y),3+x],[x,y,z] ], ",  # invalid string.
    ]
    var = ["x", "y", "z"]

    for t in test:
        s = text_to_sympy(t)
        print(
            t,
            "=>\n  valid ? with (x,y,z): ",
            is_valid_sympy(t, check_var=var),
            "\n  text:",
            text_to_list(t),
            "\n  sympy:",
            s,
            "\n  str:",
            sympy_to_str(s),
            "\n  float:",
            sympy_to_float(s),
            "\n  complex:",
            sympy_to_complex(s),
            "\n  latex:",
            sympy_to_latex(s),
            "\n  Mathematica:",
            sympy_to_mathematica(s),
        )


# ================================================== main
test_convert_util()
