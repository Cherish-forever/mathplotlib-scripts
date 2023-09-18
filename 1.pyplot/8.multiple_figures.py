import matplotlib.pyplot as plt
import numpy as np

# fmt = '[marker][line][color]' or '[color][marker][line]'
# colors:          marker:                      line:
# 'b': blue        '.': point marker            '-' : solid line style
# 'g': green       ',': pixel marker            '--': dashed line style
# 'r': red         'o': circle marker           '-.': dash-dot line style
# 'c': cyan        'v': triangle_down marker    ':' : dotted line style
# 'm': magenta     '^': triangle_up marker
# 'y': yellow      '<': triangle_left marker
# 'k': black       '>': triangle_right marker
# 'w': white       '1': tri_down marker
#                  '2': tri_up marker
#                  '3': tri_left marker
#                  '4': tri_right marker
#                  '8': octagon marker
#                  's': square marker
#                  'p': pentagon marker
#                  'P': plus (filled) marker
#                  '*': star marker
#                  'h': hexagon1 marker
#                  'H': hexagon2 marker
#                  '+': plus marker
#                  'x': x marker
#                  'X': x (filled) marker
#                  'D': diamond marker
#                  'd': thin_diamond marker
#                  '|': vline marker
#                  '_': hline marker

x = np.linspace(0, 2 * np.pi, 30)

# first figure
plt.figure()
plt.subplot(211) # the first subplot in the first figure
plt.plot(x, np.sin(x), 'bo', x, np.sin(x), 'k')
plt.subplot(212) # the second subplot in the first figure
plt.plot(x, np.sin(x), 'r--')

# second figure
plt.figure(2)
plt.subplot(211) # the first subplot in the sencod figure
plt.plot(x, np.cos(x), 'bo', x, np.cos(x), 'k')

plt.subplot(212) # the second subplot in the sencod figure
plt.plot(x, np.cos(x), 'r--')

plt.show()
