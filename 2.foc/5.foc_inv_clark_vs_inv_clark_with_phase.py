import numpy as np
import matplotlib.pyplot as plt

alphad = np.arange(0, 360, 1)
alpha = np.deg2rad(alphad)

va = np.cos(alpha)
vb = np.sin(alpha)

# inv clark
ia = va
ib = -0.5 * va + 0.8660254039 * vb
ic = -(ia + ib)

# inv clark with phase
pb = vb
pa = -0.5 * vb + 0.8660254039 * va
pc = -(pa + pb)

plt.figure(1)
plt.subplot(221)
plt.plot(alphad, ia, color="r", label="a")
plt.plot(alphad, ib, color="g", label="b")
plt.plot(alphad, ic, color="b", label="c")

plt.subplot(222)
plt.plot(alphad, pa, color="r", label="a")
plt.plot(alphad, pb, color="g", label="b")
plt.plot(alphad, pc, color="b", label="c")

plt.show()
