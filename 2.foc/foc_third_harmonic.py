import numpy as np
import matplotlib.pyplot as plt

alphad = np.arange(0, 360, 1)
alpha = np.deg2rad(alphad)

a = np.sin(alpha)
b = np.sin(alpha + (2 / 3) * np.pi)
c = np.sin(alpha - (2 / 3) * np.pi)

ta = a + 0.15 * np.sin(3 * alpha)
tb = b + 0.15 * np.sin(3 * (alpha + (2 / 3) * np.pi))
tc = c + 0.15 * np.sin(3 * (alpha - (2 / 3) * np.pi))

plt.figure(1)
plt.subplot(221)
plt.plot(alphad, a, color="r", label="a")
plt.plot(alphad, b, color="g", label="b")
plt.plot(alphad, c, color="b", label="c")

plt.subplot(222)
plt.plot(alphad, ta, color="r", label="a")
plt.plot(alphad, tb, color="g", label="b")
plt.plot(alphad, tc, color="b", label="c")

plt.show()
