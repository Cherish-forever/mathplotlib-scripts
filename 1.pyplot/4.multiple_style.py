import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 50)

# r--: red dash line
# bs : blue square
# g^ : green triangle
plt.plot(x, np.sin(x), 'r--',
         x, np.sin(x + (2 / 3) * np.pi), 'bs',
         x, np.sin(x + (4 / 3) * np.pi), 'g^')

plt.show()
