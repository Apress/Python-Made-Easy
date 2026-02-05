import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0,5,20)
y1 = x1**2
x2 = np.linspace(0,4,5)
y2 = 16-x2**2
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.savefig('images/zwei_kurven.png')