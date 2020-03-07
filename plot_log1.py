
import matplotlib.pyplot as plt
import numpy as np
import math

#x = np.arange(0, 1000, 1)
#y = [756.3 * math.log(0.02 * a + 1, 10) for a in x]
#plt.plot(x, y)
#
#y1 = [500 - 500 * math.cos(2 * math.pi * 0.0005 * b) for b in x]
#plt.plot(x, y1)

y2 = [1000 * (math.exp(0.003 * b - 2.8074) - 0.1428) for b in x]
plt.plot(x, y2)

y3 = [756.3 * math.log10(0.02 * b + 1) for b in x]
plt.plot(x, y3)

y4 = [500 - 500 * math.cos(2 * math.pi * 0.0005 * b) for b in x]
plt.plot(x, y4)


plt.show()

