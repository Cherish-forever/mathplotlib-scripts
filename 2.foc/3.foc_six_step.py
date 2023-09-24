import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle


fig, ax = plt.subplots()
line_width = 1
line_color = 'blue'
side_length = 2 / np.sqrt(3)

def circle(ax, xy=(0.0, 0.0), radius=1):
    cir1 = Circle(xy = xy, radius=radius, fill=False)
    ax.add_patch(cir1)

def hexagon(ax, side, xy=(0, 0), rotate=0, linewidth=1, color='b'):
    p0_x = np.cos(rotate) * side
    p0_y = np.sin(rotate) * side
    p1_x = side * np.cos((np.pi / 3) + rotate)
    p1_y = np.sin((np.pi / 3) + rotate) * side
    p2_x = -side * np.cos((np.pi / 3) - rotate)
    p2_y = np.sin((np.pi / 3) - rotate) * side

    x = np.array([p0_x, p1_x, p2_x, -p0_x, -p1_x, -p2_x, p0_x]) + xy[0]
    y = np.array([p0_y, p1_y, p2_y, -p0_y, -p1_y, -p2_y, p0_y]) + xy[1]

    ax.plot(x, y, linewidth=linewidth, color=color)

circle(ax, radius=1)
circle(ax, radius = 2 / np.sqrt(3))

hexagon(ax, 2 / np.sqrt(3))
hexagon(ax, 4 / 3, rotate=(np.pi / 6), color='y')

ax.plot([0, np.cos(np.pi / 6)], [0, np.sin(np.pi / 6)], color='r')

plt.annotate('SPWM', xy=(np.cos(np.pi / 3), np.sin(np.pi / 3)), xytext=(0.1, 0.6),
             arrowprops=dict(arrowstyle="->", color='r'))

plt.annotate('SVPWM', xy=(np.cos(np.pi / 6) * 1.15, np.sin(np.pi / 6) * 1.15), xytext=(1.2, 0.8),
             arrowprops=dict(arrowstyle="->", color='r'))

ax.axhline(0, ls="--")
ax.axvline(0, ls="--")

ax.axhline(1, ls="--")
ax.axhline(-1, ls="--")

ax.axvline(1, ls="--")
ax.axvline(-1, ls="--")

plt.text(side_length, 0, r'100')
plt.text(-side_length, 0, r'011', horizontalalignment='right')

plt.text(np.cos(np.pi / 3) * 1.15, np.sin(np.pi / 3) * 1.15, r'110')
plt.text(-np.cos(np.pi / 3) * 1.15, np.sin(np.pi / 3) * 1.15, r'010', horizontalalignment='right')

plt.text(np.cos(np.pi / 3) * 1.15, -np.sin(np.pi / 3) * 1.15, r'101')
plt.text(-np.cos(np.pi / 3) * 1.15, -np.sin(np.pi / 3) * 1.15, r'001', horizontalalignment='right')

# a
#plt.arrow(0, 0, 1.15, 0, color='r', head_width=0.1, head_length=0.1, length_includes_head=True, linewidth=5)

# b
#plt.arrow(0, 0, -1.15 * np.cos(np.pi / 3), 1.15 * np.sin(np.pi / 3), color='g', head_width=0.1, head_length=0.1, length_includes_head=True, linewidth=5)

# c
#plt.arrow(0, 0, -1.15 * np.cos(np.pi / 3), -1.15 * np.sin(np.pi / 3), color='b', head_width=0.1, head_length=0.1, length_includes_head=True, linewidth=5)

ax.axis('equal')
plt.show()
