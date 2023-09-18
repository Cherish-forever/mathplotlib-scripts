import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)

# plot with various axes scales
plt.figure()

# sin
plt.subplot(221)
plt.plot(x, np.sin(x))
plt.title('sin(x)')
plt.grid(True)

# cos
plt.subplot(222)
plt.plot(x, np.cos(x))
plt.title('cos(x)')
plt.grid(True)

# tan
plt.subplot(223)
plt.plot(x, np.tan(x))
plt.title('tan(x)')
plt.grid(True)

# logit
plt.subplot(224)
plt.plot(x, np.log(x))
plt.title('log(x)')
plt.grid(True)
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

plt.show()
