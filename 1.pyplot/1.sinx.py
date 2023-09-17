import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, np.sin(x))
ax.plot(x, np.sin(x + (2 / 3) * np.pi))
ax.plot(x, np.sin(x + (4 / 3) * np.pi))
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.show()
