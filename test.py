import numpy as np

from Function import *
from matplotlib import pyplot as plt


x = Function.parameter()
a = x**3
b = Sin(1/(x**2))
f = a * b

X = np.linspace(-0.2, 0.2, 1000)
Y = np.array([f(i) for i in X])

plt.plot(X, Y)
plt.show()