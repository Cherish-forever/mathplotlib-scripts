import numpy as np
import matplotlib.pyplot as plt

alphad = np.arange(0, 360, 1)
alpha = np.deg2rad(alphad)

fig, ax = plt.subplots()

ax.set_xlabel("State space vector angle (deg)")
ax.set_ylabel("Duty cycle")

da = np.array([])
db = np.array([])
dc = np.array([])

def get_sector(a, b, c):
    sector = 0
    if (c < 0):
        if (a < 0):
            sector = 2
        else:
            if (b < 0):
                sector = 6
            else:
                sector = 1
    else:
        if (a < 0):
            if (b <= 0):
                sector = 4
            else:
                sector = 3
        else:
            sector = 5

    return sector

for rad in alpha:
    va = np.cos(rad)
    vb = np.sin(rad)

    a = va
    b = -0.5 * va + 0.8660254039 * vb
    c = -(a + b)

    k = (2 / np.sqrt(3))
    a = a * k
    b = b * k
    c = c * k
    sector = get_sector(a, b, c)

    if (sector == 1):
        x = a;
        y = b;
        z = 1 - (x+y)

        a = x + y + z * 0.5
        b = y + z * 0.5
        c = z * 0.5
    elif(sector == 2):
        x = -c;
        y = -a;
        z = 1 - (x+y)

        a = x + z * 0.5
        b = x + y + z * 0.5
        c = z * 0.5
    elif(sector == 3):
        x = b;
        y = c;
        z = 1 - (x+y)

        a = z * 0.5
        b = x + y + z * 0.5
        c = y + z * 0.5
    elif(sector == 4):
        x = -a;
        y = -b;
        z = 1 - (x+y)

        a = z * 0.5
        b = x + z * 0.5
        c = x + y + z * 0.5
    elif(sector == 5):
        x = c;
        y = a;
        z = 1 - (x+y)

        a = y + z * 0.5
        b = z * 0.5
        c = x + y + z * 0.5
    elif(sector == 6):
        x = -b;
        y = -c;
        z = 1 - (x+y)

        a = x + y + z * 0.5
        b = z * 0.5
        c = x + z * 0.5
    else:
        print("Error")

    da = np.append(da, a)
    db = np.append(db, b)
    dc = np.append(dc, c)

ax.plot(alphad, da, color="r", label=r"$d_a$")
ax.plot(alphad, db, color="g", label=r"$d_b$")
ax.plot(alphad, dc, color="b", label=r"$d_c$")

ax.axvline(0, ls="--")
ax.axvline(60, ls="--")
ax.axvline(120, ls="--")
ax.axvline(180, ls="--")
ax.axvline(240, ls="--")
ax.axvline(300, ls="--")
ax.axvline(360, ls="--")

ax.axhline(0, ls="--")
ax.axhline(1, ls="--")

plt.show()

