import numpy as np
import matplotlib.pyplot as plt
from pylab import show, arange, sin, plot, pi

x = np.arange(0, 5, 0.1)
y = np.sin(x) #(numpy - funkcja sin)
plt.plot(x, y) # rysowanie (biblioteka matplotlib)

t = np.arange(0.0, 2.0, 0.01)
s = sin(2 * pi * t) #(numpy - funkcja sin)
plot(t, s)

show() # pokazuje nasze okno z wykresem