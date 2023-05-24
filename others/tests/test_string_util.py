"""
test for string_util
"""
import gcoreutils.string_util as csu


# ==================================================
def test_wrap_string():
    print("=== wrap_string ===")
    lst = ["a", ["a"], ["a", "b"], [["a", "b"], ["c", "d"]], [[["a", "b"], ["c", "d"]], [["e", "f"], ["g", "h"]]]]
    for s in lst:
        print(s, "=>", csu.wrap_string(s, "$ ", " $"))


# ==================================================
def test_table_to_str():
    print("=== table_to_str ===")
    tbl = ["a", ["a"], ["a", "b"], [["a", "b"], ["c", "d"]]]
    for t in tbl:
        print(t, "=>", csu.table_to_str(t, " & ", r" \\" + "\n"))


# ==================================================
def test_circle_number():
    print("=== circle_number ===")
    for i in range(3):
        print(csu.circle_number(i))


# ==================================================
def test_convert_to_fraction():
    print("=== convert_to_fraction ===")
    lst = ["1.23", "[1.2,3,4.3]", "1.3*x", "[1,2,sqrt(3.4)]", "1.2*(x**2+1.2*y)"]
    for s in lst:
        sr = csu.convert_to_fraction(s)
        print(s, "=>", sr)
    print(csu.convert_to_fraction(lst))


# ================================================== main
test_wrap_string()
test_table_to_str()
test_circle_number()
test_convert_to_fraction()
