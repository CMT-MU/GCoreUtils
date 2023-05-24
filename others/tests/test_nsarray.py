"""
test for nsarray
"""
import sympy as sp
import pickle
from gcoreutils.nsarray import NSArray


def test_create():
    print("=== test_create ===")
    data = [
        "(1+I)sin(x)",  # scalar
        "{E}",  # scalar (list)
        "{E,pi,I}",  # scalar (list)
        "{{x,y,z},{1,2,3},{4,5,6}}",  # scalar (list)
        "[1,2,3]",  # vector
        "{[x,y,z]}",  # vector (list)
        "{[x,y,z],[1,2,3],[4,5,6]}",  # vector (list)
        "[[1,2],[3,4]]",  # matrix
        "{[[1,2],[3,4]]}",  # matrix
        "{[[1,2],[3,4]],[[5,6I],[7x,8y]],[[11,12],[13,14]]}",  # matrix (list)
        "[1/2,3/2,1]@[0,0,0]",  # bond
        "{[1/2,3/2,1]@[0,0,0]}",  # bond
        "{[3/2,1,1/2]@[1,2,3],[2,2,2]@[1,1,1],[3,3,3]@[1/2,1/2,1/2]}",  # bond (list)
        "[0,0,0];[1,1,1]",  # bond_th
        "{[0,0,0];[1,1,1],[1,1,1];[2,2,2],[3,3,3];[1/2,1/2,1/2]}",  # bond_th (list)
        "[0,0,0]:[1,1,1]",  # bond_sv
        "{[0,0,0]:[1,1,1],[1,1,1]:[2,2,2],[3,3,3]:[1/2,1/2,1/2]}",  # bond_sv (list)
    ]
    subs = {"x": sp.pi / 2, "y": 2, "z": 3}

    for i in data:
        a = NSArray(i)
        print(a)
        print("len:", len(a))
        print("shape:", a.shape)
        print(repr(a))
        print("value(x=pi/2,y=2,z=3):", repr(a.value(subs)))
        print("sympy:", repr(a.sympy()))
        print("str:", a.str())
        print("latex:", a.latex())
        if a.lst:
            print("a[0]:", repr(a[0]))
            print("a[1:]:", repr(a[1:]))
            if isinstance(a[0], NSArray) and a[0].style in ["scalar", "vector", "matrix"]:
                print("a[0][0]:", repr(a[0][0]))
            for i, ai in enumerate(a):
                print(f"  a[{i}] =", repr(ai))
        if a.style in ["bond"]:
            print("tail-head:", *a.convert_bond("bond_th"))
            print("start-vector:", *a.convert_bond("bond_sv"))
        print("---")


def test_bond_conversion():
    print("=== test_bond_conversion ===")
    data = [
        "[1/2,3/2,1]@[0,0,0]",  # bond
        "{[3/2,1,1/2]@[1,2,3],[2,2,2]@[1,1,1]}",  # bond (list)
        "[0,0,0];[1,1,1]",  # bond_th
        "{[0,0,0];[1,1,1],[1,1,1];[2,2,2]}",  # bond_th (list)
        "[0,0,0]:[1,1,1]",  # bond_sv
        "{[0,0,0]:[1,1,1],[1,1,1]:[2,2,2]}",  # bond_sv (list)
    ]
    for i in data:
        a = NSArray(i)
        print(a)
        print("vc:", a.convert_bond("bond"))
        print("th:", a.convert_bond("bond_th"))
        print("sv:", a.convert_bond("bond_sv"))
        print("---")


def test_create_bond_pair():
    b1 = NSArray("{[1,2],[3,4]}")
    b2 = NSArray("{[11,12],[13,14]}")
    print("b1:", b1, "| b2:", b2)
    print("bond:", repr(NSArray.create_bond_from_pair(b1, b2, "bond")))
    print("bond_th:", repr(NSArray.create_bond_from_pair(b1, b2, "bond_th")))
    print("bond_sv:", repr(NSArray.create_bond_from_pair(b1, b2, "bond_sv")))


def test_sort():
    print("=== test_sort ===")
    lst = [
        "{[sqrt(3)/2,E,1],[sqrt(3)/2,E-1,1/2]}",
        "{ [[pi,E],[sqrt(3),4],[5,6]], [[pi,E],[1,3],[6,5]] }",
        "{ {{{11,21},{31,41},{51,61}}, {{pi,E},{sqrt(3/2),4},{5,6}}}, {{{11,5},{4,3},{2,1}}, {{3,2},{1,3},{2*pi,E/3}}} }",
        "{ [2,2,2]@[1,1,1], [3/2,1,1/2]@[1,1,1] }",
    ]
    for i in lst:
        s = NSArray(i)
        ss = s.sort()
        print(s, "=>")
        for i in ss:
            print(" ", i)
        print("---")


def test_reverse_direction():
    print("=== test_reverse_direction ===")
    data = [
        "[0,-1,1]@[1,2,3]",
        "{ [0,0,-1]@[1,2,3], [-1,1,1]@[1,2,3] }",
        "[0,-1,1];[1,2,3]",
        "{ [0,0,-1];[1,2,3], [-1,1,1];[1,2,3] }",
        "[0,-1,1]:[1,2,3]",
        "{ [0,0,-1]:[1,2,3], [-1,1,1]:[1,2,3] }",
    ]
    for i in data:
        s = NSArray(i)
        print(s, "=>", repr(s.reverse_direction()))
        print("---")


def test_regular_direction():
    print("=== test_regular_direction ===")
    data = [
        "[0,-1,1]@[1,2,3]",
        "{ [0,0,-1]@[1,2,3], [-1,1,1]@[1,2,3] }",
        "[1,3,1];[1,2,3]",
        "{ [1,0,-1];[1,2,3], [1,3,1];[1,2,3] }",
        "[0,-1,1]:[-1,2,3]",
        "{ [0,0,-1]:[0,-2,3], [-1,1,1]:[0,0,-3] }",
    ]
    for i in data:
        s = NSArray(i)
        print(s, "=>", repr(s.regular_direction()))
        print("---")


def test_simplify():
    print("=== test_simplify ===")
    data = [
        "(1+I)/(1-I)",  # scalar
        "{E,pi/sqrt(3),I/(1+I)}",  # scalar (list)
        "[1/(3+4),(1+I)/(1-I),3]",  # vector
        "{[1,2,3],[4,5/(sqrt(2)**2+3),(1+I)/(1-I)]}",  # vector (list)
    ]
    for i in data:
        s = NSArray(i)
        print(s, "=>", repr(s.simplify()))


def test_index():
    print("=== test_index ===")
    data = [
        "{ [sqrt(3)/2,E,1], [sqrt(3)+1,E-1,1/2] }",
        "{ [[1,2],[3,4],[5,6]], [[x,y],[z,4],[5,6]] }",
        "{ {{{1,2},{3,4},{5,6}}, {{x,y},{z,4},{5,6}}}, {{{6,5},{4,3},{2,1}}, {{3,2},{1,x},{y,z}}} }",
        "{ [3/2,1,1/2]@[1,2,3], [2,2,2]@[1,1,1] }",
    ]
    key = ["[sqrt(3)+1,E-1,1/2]", "[[x,y],[z,4],[5,6]]", "3", "[2,2,2]@[1,1,1]"]

    for i, j in zip(data, key):
        s = NSArray(i)
        print("find", j, "in", s)
        idx = s.index(j)
        if idx:
            print("index =", idx, ", item =", s[idx])
        else:
            print("not found.")
        print("---")


def test_remove_duplicate():
    print("=== test_remove_duplicate ===")
    lst = [
        "{ {{{1,2},{3,4},{5,6}}, {{x,y},{z,4},{5,6}}}, {{{6,5},{4,3},{2,1}}, {{3,2},{1,x},{y,z}}} }",
        "{[sqrt(3)/2,E,y],[sqrt(3)+1,E-1,1/2],[sqrt(3)/2,E,y]}",
        "{ [3/2,1,1/2]@[1,2,x], [2,2,2]@[1,1,1], [3/2,1,1/2]@[1,2,x] }",
        "{[sqrt(3)/2,E,y],[sqrt(3)/2,E,y]}",
        "{ [3/2,1,1/2]@[1,2,x], [3/2,1,1/2]@[1,2,x] }",
    ]
    for i in lst:
        s = NSArray(i)
        print(s, "=>")
        print(repr(s.remove_duplicate(sort=False)))
        print("---")


def test_transform():
    print("=== test_transform ===")
    lst = [
        "[1,1,1]",
        "{[1,1,1],[x,y,z]}",
        "[[1,-1/2,0],[0,sqrt(3)/2,0],[0,0,1]]",
        "{ [[0,1,0],[1,0,0],[0,0,1]], [[0,2,0],[1,2,0],[0,0,1]] }",
        "[0,0,0];[0,1,0]",
        "{ [0,0,0];[0,1,0], [1,1,1];[2,2,2] }",
    ]
    A = NSArray("[[1,-1/2,0],[0,sqrt(3)/2,0],[0,0,1]]")
    A4 = NSArray("[[1,-1/2,0,1/2],[0,sqrt(3)/2,0,0],[0,0,1,0],[0,0,0,1]]")
    for i in lst:
        s = NSArray(i)
        print("A :", s, "=>", s.transform(A))
        print("A4:", s, "=>", s.transform(A4))
        print("---")


def test_apply():
    print("=== test_apply ===")
    lst = [
        "[1,1,1]",
        "[[1,-1/2,0],[0,sqrt(3)/2,0],[0,0,1]]",
        "[0,0,0];[0,1,0]",
    ]
    A = NSArray("{ [[1,-1/2,0],[0,sqrt(3)/2,0],[0,0,1]], [[1,0,0],[0,2,0],[0,0,1]] }")
    for i in lst:
        s = NSArray(i)
        print("A *", s, "=>", repr(A.apply(s)))
        print("---")


def test_sum():
    print("=== test_sum ===")
    lst = [
        "{[0, 1, 1, 0],[0, -I, I, 0],[1, 0, 0, -1],[1, -I, I, 1],[x, y, 1, -2]}",
        "{{0, 1, 1, 0},{0, -I, I, 0},{1, 0, 0, -1},{1, -I, I, 1},{x, y, 1, -2}}",
    ]
    for i in lst:
        s = NSArray(i)
        print(s, "=>", repr(s.sum()))
        print("---")


def test_norm():
    print("=== test_norm ===")
    lst = [
        "sin(x)",
        "[E,pi,1]",
        "{[sqrt(3)/2,E,1],[sqrt(3)+1,E-1,1/2]}",
        "[[sqrt(3)/2,E,1],[sqrt(3)+1,E,1]]",
        "{ [[1,2],[3,4],[5,6]], [[x,y],[z,4],[5,6]] }",
        "{ {{{1,2},{3,4},{5,6}}, {{x,y},{z,4},{5,6}}}, {{{6,5},{4,3},{2,1}}, {{3,2},{1,x},{y,z}}} }",
        "[1/2,3/2,1]@[0,0,0]",
        "{ [3/2,1,1/2]@[1,2,3], [2,2,2]@[1,1,1] }",
    ]
    for i in lst:
        a = NSArray(i)
        print(a, "=>", repr(a.norm()))
        print("---")


def test_normalize():
    print("=== test_normalize ===")
    a = NSArray("{[1,1,1],[0,0,0]}")
    na, n = a.normalize(ret_norm=True)
    print(repr(na))
    print(repr(n))


def test_3d_vector():
    print("=== test_3d_vector ===")
    head = ["Q", "G", "T", "M"]
    for i in head:
        s = NSArray.vector3d(i)
        print(repr(s))


def test_shift():
    print("=== test_shift ===")
    lst = [
        "[1,1,1]",
        "{[1,x+1,1],[2,2,y-2]}",
        "[[1,-1/2,0],[0,sqrt(3)/2,0],[0,0,1]]",
        "{ {{{1,2},{3,4},{5,6}}, {{x,y},{z,4},{5,6}}}, {{{6,5},{4,3},{2,1}}, {{3,2},{1,x},{y,z}}} }",
        "[1,x,-1/2]@[-1/2,2/3,y]",
        "{ [1,x,-1/2]@[-1/2,2/3,y], [-1/2,x,x-1/2]@[1,x,x-y] }",
        "[1,x,-1/2];[-1/2,2/3,y]",
    ]
    for i in lst:
        s = NSArray(i)
        print("---", s)
        shifted, s = s.shift(with_shift=True)
        print("shifted:", repr(shifted))
        print("shift:  ", repr(s))


def test_clip():
    print("=== test_clip ===")
    lst = ["{ [1,0,0], [0,1,0], [1,1,1] }", "{[0,0,0];[1,0,0], [0,0,0];[0,1,0],[0,0,0];[1,1,1]}"]
    for i in lst:
        s = NSArray(i)
        idx = s.clip([-0.1, -0.5, -0.5], [1.1, 1.5, 0.5])
        print(idx, repr(s[idx]))


def test_distance():
    print("=== test_distance ===")
    s1 = "{ [sqrt(3)/2,E,1], [sqrt(3)+1,E-1,1/2], [1,2,3],[4,5,6],[3,5,6] }"
    s2 = "{ [sqrt(3)/2,E,1], [sqrt(3)+1,E-1,1/2], [1,2,3],[4,5,6],[3,5,6] }"
    a1 = NSArray(s1)
    a2 = NSArray(s2)
    for i, j in NSArray.distance(a1, a1).items():
        print(i, j)
    print("---")
    for i, j in NSArray.distance(a1, a2).items():
        print(i, j)


def test_igrid():
    print("=== test_igrid ===")
    N = [2, 2, 2]
    offset = [-1, 3, 2]
    g = NSArray.igrid(N, offset)
    print(repr(g))


def test_grid():
    print("=== test_grid ===")
    xs = [-1, -1, -1]
    xe = [1, 1, 1]
    N = [10, 2, 2]
    g = NSArray.grid(xs, xe, N)
    print(repr(g))


def test_grid_path():
    print("=== test_grid_path ===")
    pts = {"A": [0, 0], "B": [1, 0], "C": [1, 1], "D": [-1, -1]}
    gpath = "A-B-C-A|D-A"
    A = NSArray("[[1,-1/2],[0,sqrt(3)/2]]", fmt="value")
    grid, glin, gdis = NSArray.grid_path(pts, gpath, 4, A)
    print("grid:", repr(grid))
    print("linear pos:", repr(glin))
    print("disc. pos.", gdis)


def test_orthogonalize():
    print("=== test_orthogonalize ===")
    v = NSArray("{[0, 1, 1, 0],[0, -I, I, 0],[1, 0, 0, -1],[1, -I, I, 1],[2, 1, 1, -2]}")
    vo, idx = NSArray.orthogonalize(v)
    vo = vo.remove(idx)
    print(repr(vo), repr(idx))
    t = [[NSArray.dot(i, j) for j in vo] for i in vo]
    print("check:", t)

    v = NSArray(
        "{[[0, 1, 1, 0], [0, 1, 1, 0]],[[0, -I, I, 0], [0, -I, I, 0]],[[1, 0, 0, -1], [1, 0, 0, -1]],[[1, -I, I, 1], [1, -I, I, 1]]}"
    )
    vo, idx = NSArray.orthogonalize(v)
    vo = vo.remove(idx)
    print(repr(vo), repr(idx))
    t = [[NSArray.dot(i, j) for j in vo] for i in vo]
    print("check:", t)


def test_lambdify():
    print("=== test_lambdify ===")
    h = "[[e1, t*sin(k1)+I], [t*sin(k1)-I, e2]]"
    h1 = "[[0, sin(k1)], [sin(k1), 0]]"
    H = NSArray(h)
    H1 = NSArray(h1)

    f = H.lambdify()
    p = NSArray("{[1, 2, 3, 4], [2, 3, 4, 1]}")
    print(f.__doc__)
    print(repr(f(p)))
    print(repr(f(p[0])))

    f1 = H1.lambdify()
    print(f1.__doc__)
    print(repr(f1([1, 2])))
    print(repr(f1(1)))


def test_eigen():
    print("=== test_eigen ===")
    params = NSArray("{[1, 2, 0.0], [1, 2, 0.1], [1, 2, 0.2], [1, 2, 0.3], [1, 2, 0.4], [1, 2, 0.5]}")
    h = NSArray("[[e1, sin(v)], [sin(v), e2]]")
    print("(e1,e2,v) =", params)
    f, vals, vecs = h.diagonalize_hermite(params)
    print(f.__doc__)
    print("--- eigenvalues")
    print(repr(vals))
    print("--- eigenvectors")
    print(repr(vecs))


def test_eigen2():
    print("=== test_eigen2 ===")
    h = NSArray("{ [[0,1], [1,0]], [[0,-I], [I,0]], [[1,0], [0,-1]] }", fmt="value")
    f, vals, vecs = h.diagonalize_hermite()
    print(f.__doc__)
    print("--- eigenvalues")
    print(repr(vals))
    print("--- eigenvectors")
    print(repr(vecs))


def test_pickle():
    print("=== test_pickle ===")
    data = [
        "(1+I)sin(x)",  # scalar
        "{E}",  # scalar (list)
        "{E,pi,I}",  # scalar (list)
        "{{x,y,z},{1,2,3},{4,5,6}}",  # scalar (list)
        "[1,2,3]",  # vector
        "{[x,y,z]}",  # vector (list)
        "{[x,y,z],[1,2,3],[4,5,6]}",  # vector (list)
        "[[1,2],[3,4]]",  # matrix
        "{[[1,2],[3,4]]}",  # matrix
        "{[[1,2],[3,4]],[[5,6I],[7x,8y]],[[11,12],[13,14]]}",  # matrix (list)
        "[1/2,3/2,1]@[0,0,0]",  # bond
        "{[1/2,3/2,1]@[0,0,0]}",  # bond
        "{[3/2,1,1/2]@[1,2,3],[2,2,2]@[1,1,1],[3,3,3]@[1/2,1/2,1/2]}",  # bond (list)
        "[0,0,0];[1,1,1]",  # bond_th
        "{[0,0,0];[1,1,1],[1,1,1];[2,2,2],[3,3,3];[1/2,1/2,1/2]}",  # bond_th (list)
        "[0,0,0]:[1,1,1]",  # bond_sv
        "{[0,0,0]:[1,1,1],[1,1,1]:[2,2,2],[3,3,3]:[1/2,1/2,1/2]}",  # bond_sv (list)
    ]
    d = [NSArray(i) for i in data]
    with open("nsarray.pkl", "wb") as f:
        pickle.dump(d, f)

    with open("nsarray.pkl", "rb") as f:
        dd = pickle.load(f)

    for i, j in zip(d, dd):
        print(repr(i))
        print(repr(j))
        print("---")


def test_from_str():
    print("=== test_from_str ===")
    data = [
        ["(1+I)sin(x)"],
        ["E", "pi", "I"],
        ["[1,2,3]"],
        ["[x,y,z]", "[1,2,3]", "[4,5,6]"],
        ["[[1,2],[3,4]]"],
        ["[[1,2],[3,4]]", "[[5,6I],[7x,8y]]", "[[11,12],[13,14]]"],
        ["[1/2,3/2,1]@[0,0,0]"],
        ["[3/2,1,1/2]@[1,2,3]", "[2,2,2]@[1,1,1]", "[3,3,3]@[1/2,1/2,1/2]"],
        ["[1/2,3/2,1];[0,0,0]"],
        ["[3/2,1,1/2];[1,2,3]", "[2,2,2];[1,1,1]", "[3,3,3];[1/2,1/2,1/2]"],
        ["[1/2,3/2,1]:[0,0,0]"],
        ["[3/2,1,1/2]:[1,2,3]", "[2,2,2]:[1,1,1]", "[3,3,3]:[1/2,1/2,1/2]"],
    ]
    for d in data:
        s = NSArray.from_str(d)
        print(d, "=>", repr(s))


# ================================================== main test
test_create()
test_bond_conversion()
test_create_bond_pair()
test_sort()
test_reverse_direction()
test_regular_direction()
test_simplify()
test_index()
test_remove_duplicate()
test_transform()
test_apply()
test_sum()
test_norm()
test_normalize()
test_3d_vector()
test_shift()
test_clip()
test_distance()
test_igrid()
test_grid()
test_grid_path()
test_orthogonalize()
test_lambdify()
test_eigen()
test_eigen2()
test_pickle()
test_from_str()
