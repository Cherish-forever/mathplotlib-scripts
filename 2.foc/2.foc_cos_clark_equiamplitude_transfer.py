import numpy as np
import matplotlib.pyplot as plt

alphad = np.arange(0, 360, 1)
alpha = np.deg2rad(alphad)

a = np.cos(alpha)
b = np.cos(alpha + (2 / 3) * np.pi)
c = np.cos(alpha - (2 / 3) * np.pi)

# befor equiamplitude
va1 = (3 / 2) * a
vb1 = (np.sqrt(3) / 2) * a + np.sqrt(3) * b

# after equiamplitude
va2 = va1 * (2 / 3)
vb2 = vb1 * (2 / 3)

# inv clark
ta = va2
tb = vb2 * (3 / 2 / np.sqrt(3)) - (1 / 2) * va2
#tb = vb2 * 0.8660254039 - 0.5 * va2
tc = -(ta + tb)

plt.figure(1)
plt.subplot(221)
plt.plot(alphad, a, color="r", label="a")
plt.plot(alphad, b, color="g", label="b")
plt.plot(alphad, c, color="b", label="c")

plt.subplot(222)
plt.plot(alphad, va1, color="#ff81c0", label="va")
plt.plot(alphad, vb1, color="#c081ff", label="vb")

plt.subplot(223)
plt.plot(alphad, va2, color="#ff81c0", label="va")
plt.plot(alphad, vb2, color="#c081ff", label="vb")

plt.subplot(224)
plt.plot(alphad, ta, color="r", label="a")
plt.plot(alphad, tb, color="g", label="b")
plt.plot(alphad, tc, color="b", label="c")

plt.show()
