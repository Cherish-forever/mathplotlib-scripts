import matplotlib.pyplot as plt
import numpy as np

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probabitlity')

# TeX or LaTeX
# https://matplotlib.org/stable/users/explain/text/mathtext.html#mathtext
# https://matplotlib.org/stable/users/explain/text/usetex.html#usetex
plt.title(r'$\sigma_i=15$')

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')

plt.axis([40, 160, 0, 0.03])
plt.grid(True)

plt.show()
