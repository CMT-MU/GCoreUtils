"""
test for pdf_via_latex
"""
from gcoreutils.pdf_via_latex import PDFviaLaTeX

test_dir = __file__[: __file__.rfind("/")]


# ==================================================
def test_pdf():
    pdf = PDFviaLaTeX("foo", dir=test_dir)

    # タイトル
    pdf.title("お試し")

    # 数式
    pdf.text(r"\section{数式、複数数式、長い数式}")
    eq1 = r"\int dx f(x)"
    eq2 = r"\Gamma_{\alpha\beta\gamma\delta}(1,2;3,4)= \frac{1}{2}(\delta_{\alpha\gamma}\delta_{\beta\delta} -\delta_{\alpha\delta}\delta_{\beta\gamma}) [\Gamma(1,2;3,4)+\Gamma(1,2;4,3)] +\frac{1}{2}(\delta_{\alpha\gamma}\delta_{\beta\delta} +\delta_{\alpha\delta}\delta_{\beta\gamma}) [\Gamma(1,2;3,4)-\Gamma(1,2;4,3)]"
    eqs = [r"a_{11} = 1", r"b_{22} = 2"]

    pdf.equation(eq1)
    pdf.equation(eq2, long=True)
    pdf.equation(eqs, num=True)

    # 表
    pdf.text(r"\section{枠なしテーブル}")
    rc = r"\#"
    row = ["0", "1", "2", "3"]
    col = ["a", "b", "c", "d", "e", "f"]
    tbl = [[f"{i}{j}" for j in col] for i in row]
    pdf.simple_table(tbl, cols=7, tmath=True)
    hl = [1, 2]

    pdf.text(r"\section{表}")
    pdf.table(tbl, row, col, rc, hl=hl, tmath=True)
    pdf.text()
    pdf.table(tbl, row, col, rc, hl=hl, caption="simple table", tmath=True)

    # 長い表
    pdf.text(r"\section{長い表}")
    row = list(range(30))
    tbl = [[f"{i}{j}" for j in col] for i in row]
    pdf.table(tbl, row, col[:4], rc, hl=True, caption="sample long table", stretch=1.5, tmath=True, long=True)

    # 図 (実行パスに fig.eps を置くこと)
    pdf.text(r"\section{図}")
    pdf.figure("fig.eps", width=0.5, caption="sample figure")


# ================================================== main
test_pdf()
