"""
test for latex_util
"""
from gcoreutils.latex_util import check_latex_installed, latex_version, latex_setting


# ==================================================
def test_latex():
    print("=== latex check ===")
    if check_latex_installed():
        print("LaTeX is installed.")
        print(latex_version())
        latex_setting("standard")
    else:
        print("LaTeX is not installed.")


# ================================================== main
test_latex()
