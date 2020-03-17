'''
  a.py
'''

from numpy import *
from pylab import *

x = linspace(-3, 3, 30)
y = x**2
plot(x, y)
show()

x = linspace(-3, 3, 30)
y = x**2
plot(x, y, 'r.')
show()

plot(x, sin(x))
plot(x, cos(x), 'r-')
plot(x, -sin(x), 'g--')
show()

#################################################################
'''
  b.py
'''
from matplotlib import pyplot as plt
import numpy as np
import math
x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_title("sine wave")
ax.set_xlabel('angle')
ax.set_ylabel('sine')
plt.show()
