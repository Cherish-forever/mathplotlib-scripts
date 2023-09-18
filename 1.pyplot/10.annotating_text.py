import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)

plt.plot(x, np.sin(x))
plt.annotate('max: sin(pi / 2)', xy=((np.pi / 2), 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='red', shrink=0.05))
plt.ylim(-2, 2)
plt.grid(True)

plt.show()
