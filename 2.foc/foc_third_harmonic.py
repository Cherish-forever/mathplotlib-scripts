import numpy as np
import matplotlib.pyplot as plt

alphad = np.arange(0, 360, 1)
alpha = np.deg2rad(alphad)

va = np.cos(alpha)
vb = np.sin(alpha)

a = va
b = vb * 0.8660254039 - 0.5 * va
c = -(a + b)

oa = va - (1 / np.sqrt(3) * vb)
ob = 2.0 / np.sqrt(3) * vb
oc = -(oa + ob)

ta = a + 0.15 * np.sin(3 * (alpha - np.deg2rad(30)))
tb = b + 0.15 * np.sin(3 * ((alpha + (2 / 3) * np.pi) - np.deg2rad(30)))
tc = c + 0.15 * np.sin(3 * ((alpha - (2 / 3) * np.pi) - np.deg2rad(30)))

ota = oa + 0.15 * np.sin(3 * alpha)
otb = ob + 0.15 * np.sin(3 * (alpha + (2 / 3) * np.pi))
otc = oc + 0.15 * np.sin(3 * (alpha - (2 / 3) * np.pi))

plt.figure(1)
plt.subplot(221)
plt.plot(alphad, a, color="r", label="a")
plt.plot(alphad, b, color="g", label="b")
plt.plot(alphad, c, color="b", label="c")

plt.subplot(222)
plt.plot(alphad, oa, color="r", label="a")
plt.plot(alphad, ob, color="g", label="b")
plt.plot(alphad, oc, color="b", label="c")

plt.subplot(223)
plt.plot(alphad, ta, color="r", label="a")
plt.plot(alphad, tb, color="g", label="b")
plt.plot(alphad, tc, color="b", label="c")

plt.subplot(224)
plt.plot(alphad, ota, color="r", label="a")
plt.plot(alphad, otb, color="g", label="b")
plt.plot(alphad, otc, color="b", label="c")

plt.show()
