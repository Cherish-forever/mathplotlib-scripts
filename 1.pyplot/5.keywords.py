import matplotlib.pyplot as plt
import numpy as np

data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}

# 'a'
# np.arange([start, ]stop, [step, ]dtype=None, *, like=None)
# return evenly spaced values within a given interval
# np.arange(stop): [0, stop)
# np.arange(start, stop): [start, stop)
# np.arange(start, stop, step): [start, stop) with given step

# 'b' and 'd'
# np.random.randn(d0, d1, ..., dn)
# return a sample (or samples) from the "standard normal" distribution.
# argument is dimensions of return array, must be non-negative
# if no argument a single python float is return.

# 'c'
# np.random.randint(low, high=None, size=None, dtype=int)
# return random integers from low(inclusive) to high (exclusive).

data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('x label')
plt.ylabel('y label')
plt.show()
