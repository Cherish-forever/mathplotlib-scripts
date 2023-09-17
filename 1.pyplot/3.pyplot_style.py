import matplotlib.pyplot as plt

# default is 'b-' is blue line
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'b-')

# 'ro' is red circles
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')

# 'g^' is green trigangles
plt.plot([1, 2, 3, 4], [4, 3, 2, 1], 'g^')

# [xmin, xmax, ymin, ymax] [0-6, 0-20]
plt.axis((0, 6, 0, 20))

plt.show()
