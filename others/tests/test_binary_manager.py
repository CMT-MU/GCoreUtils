"""
test for binary_manager
"""
from gcoreutils.binary_manager import BinaryManager
from gcoreutils.nsarray import NSArray


# ==================================================
class TestClass:
    def __init__(self):
        self.data = NSArray("[1,x]")

    def show(self):
        print(repr(self.data))


# ==================================================
def test_save():
    print("=== test_binary_manager (save) ===")
    bm = BinaryManager(__file__)
    bm[TestClass]
    print(*bm.keys())


# ==================================================
def test_load():
    print("=== test_binary_manager (load) ===")
    bm = BinaryManager(__file__)
    a = bm[TestClass]
    a.show()


# ================================================== main
test_save()
test_load()
