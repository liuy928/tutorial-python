import matplotlib.pyplot as plt
import random
import numpy
import math

x = numpy.arange(0, 1001, 1)

y0 = [0.7563 * math.log(0.02 * a + 1, 10) for a in x]
y1 = [2 ** (0.003 * a - 2.8124) - 0.139 for a in x]
y2 = [0.5 - 0.5 * math.cos(2 * math.pi * 0.0005 * a) for a in x]
y3 = [0.001 * a for a in x]

plt.plot(x, y0)
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.show()
