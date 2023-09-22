import numpy as np
import matplotlib.pyplot as plt

def svpwm(sector, a, b, c):
    if sector == 1:
        x = a
        y = b
        z = -(x + y)

        da = x + y + 0.5 * z
        db = y + 0.5 * z
        dc = 0.5 * z
    elif sector == 2:
        x = -c
        y = -a
        z = -(x + y)

        da = x + 0.5 * z
        db = x + y + 0.5 * z
        dc = 0.5 * z
    elif sector == 3:
        x = b
        y = c
        z = -(x + y)

        da = 0.5 * z
        db = x + y + 0.5 * z
        dc = y + 0.5 * z
    elif sector == 4:
        x = -a
        y = -b
        z = -(x + y)

        da = 0.5 * z
        db = x + 0.5 * z
        dc = x + y + 0.5 * z
    elif sector == 5:
        x = c
        y = a
        z = -(x + y)

        da = y + 0.5 * z
        db = 0.5 * z
        dc = x + y + 0.5 * z
    elif sector == 6:
        x = -b
        y = -c
        z = -(x + y)

        da = x + y + 0.5 * z
        db = 0.5 * z
        dc = x + 0.5 * z
    return da * 2, db * 2, dc *2


def calc(sector, angle):
    alpha = np.deg2rad(angle)

    va = np.cos(alpha)
    vb = np.sin(alpha)

    # amplitude assumed sqrt(3) / 2 (maximum)
    a = va - (1 / np.sqrt(3) * vb)
    b = 2.0 / np.sqrt(3) * vb
    c = -(a + b)

    return svpwm(sector, a, b, c)

def calc_offset(sector, angle):
    alpha = np.deg2rad(angle)

    va = np.cos(alpha)
    vb = np.sin(alpha)

    a = (2 / np.sqrt(3)) * va
    b = vb - (1 / np.sqrt(3)) * va
    c = -(a + b)

    return svpwm(sector, a, b, c)

fig, (ax, ax2) = plt.subplots(1, 2)

ax.set_xlabel("State space vector angle (deg)")
ax.set_ylabel("Duty cycle")

alpha = np.array([])
alpha_offset = np.array([])
da = np.array([])
db = np.array([])
dc = np.array([])

ta = np.array([])
tb = np.array([])
tc = np.array([])

for sector in range(1, 7):
    alpha_ = np.arange(60 * (sector - 1), 60 * sector, 1)
    alpha_offset_ = np.arange(60 * (sector - 1) + 30, 60 * sector + 30, 1)
    da_, db_, dc_ = calc(sector, alpha_)
    ta_, tb_, tc_ = calc_offset(sector, alpha_offset_)

    alpha = np.append(alpha, alpha_)
    alpha_offset = np.append(alpha_offset, alpha_offset_)
    da = np.append(da, da_)
    db = np.append(db, db_)
    dc = np.append(dc, dc_)
    ta = np.append(ta, ta_)
    tb = np.append(tb, tb_)
    tc = np.append(tc, tc_)

ax.plot(alpha, da, color="r", label=r"$d_a$")
ax.plot(alpha, db, color="g", label=r"$d_b$")
ax.plot(alpha, dc, color="b", label=r"$d_c$")

ax2.plot(alpha_offset, ta, color="r", label=r"$d_a$")
ax2.plot(alpha_offset, tb, color="g", label=r"$d_b$")
ax2.plot(alpha_offset, tc, color="b", label=r"$d_c$")

ax.axvline(0, ls="--")
ax.axvline(60, ls="--")
ax.axvline(120, ls="--")
ax.axvline(240, ls="--")
ax.axvline(300, ls="--")
ax.axvline(360, ls="--")

ax2.axvline(0, ls="--")
ax2.axvline(60, ls="--")
ax2.axvline(120, ls="--")
ax2.axvline(240, ls="--")
ax2.axvline(300, ls="--")
ax2.axvline(360, ls="--")


ax.legend(loc="upper right")

plt.show()
