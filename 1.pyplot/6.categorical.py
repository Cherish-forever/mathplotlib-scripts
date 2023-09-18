import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(x, np.sin(x))

plt.subplot(132)
plt.scatter(x, np.cos(x))

plt.subplot(133)
plt.plot(x, np.tan(x))

plt.suptitle('Categorical Plotting')
plt.show()
