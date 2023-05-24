"""
test for plot_util
"""
from gcoreutils.plot_util import init_plot, plot_colormap_line
import numpy as np


# ==================================================
def test_plot():
    plt, figure = init_plot()
    grid = plt.GridSpec(1, 1, hspace=0.1, wspace=0.07, width_ratios=[1], height_ratios=[1])
    ax = figure.add_subplot(grid[0, 0], xticklabels=[])

    x = np.linspace(0, 2, 100)
    y = np.array([np.sin(np.pi * x).tolist(), np.cos(np.pi * x).tolist(), (x**2 / 4).tolist()]).T
    c = np.array([np.sin(np.pi * x).tolist(), np.cos(np.pi * x).tolist(), (x**2 / 4).tolist()]).T

    ax.set_xlim(0, 2)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel("$x / \pi$")
    ax.set_ylabel("$\sin(x), \cos(x), x^2/4$")

    plot_colormap_line(x, y, c, c_range=(-1, 1), ax=ax)

    plt.show()


# ================================================== main
test_plot()
