"""
test for color_palette
"""
import gcoreutils.color_palette as cp


# ==================================================
def test_all_colors():
    print("=== all colors ===")
    for name, value in cp.all_colors.items():
        print(f"{name} = {value[0]}, {value[1]}RGB")
    print("- Apple and matplotlib colors are separated at", cp.all_colors_sep)


# ==================================================
def test_all_colormaps():
    print("=== all colormaps ===")
    for name in cp.all_colormaps:
        print(f"{name}")
    print("- Colormap categories are separated at", cp.all_colormaps_sep)


# ================================================== main
test_all_colors()
test_all_colormaps()
