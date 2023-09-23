import numpy as np
import matplotlib.pyplot as plt

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


fig, ax = plt.subplots()

hexagon(ax, 1)
hexagon(ax, 2, rotate=(np.pi / 6), color='r')

ax.axis('equal')
plt.show()
