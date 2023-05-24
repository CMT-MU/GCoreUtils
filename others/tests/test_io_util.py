"""
test for io_util
"""
from gcoreutils.io_util import write_jsonc, read_jsonc, write_dict, read_dict


# ==================================================
def test_io_util():
    dic = {
        "str": "string",
        "int": 1,
        "float": 1.2,
        "bool": True,
        "list": [1, 2, 3],
        "slist": "[x y z, [a], b]",
    }

    print("=== JSON ===")
    fn = "dict_test.json"
    write_jsonc(fn, dic, "comment")
    d = read_jsonc(fn)
    for k, v in d.items():
        print(k, v, type(v))

    print("=== dict ===")
    fn = "dict_test.py"
    write_dict(fn, dic, "comment", "dic")
    d = read_dict(fn)
    for k, v in d.items():
        print(k, v, type(v))


# ================================================== main
test_io_util()
