"""
test for list_util
"""
import gcoreutils.list_util as clu


# ==================================================
def test_list_to_table():
    print("=== list_to_table ===")
    tbl = [0, "1", 2, 3, "4", 5]
    print("original =", tbl)
    print("table without padding =", clu.list_to_table(tbl, 4))
    print("table with padding =", clu.list_to_table(tbl, 4, "-"))


# ==================================================
def test_regularize_table():
    print("=== regularize_table ===")
    tbl = [[0, "a"], ["b"], [1, "e"], ["f"]]
    print("original =", tbl)
    print("regularized =", clu.regularize_table(tbl, "---"))


# ================================================== main
test_list_to_table()
test_regularize_table()
