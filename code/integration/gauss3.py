import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 0, 100)

x2 = np.linspace(-1, 0, 4)
x2_durchschnitt = (x2[1:]+ x2[:-1])/2

def gauss(x):
    return np.exp(-x**2)

plt.plot(x, gauss(x))
plt.plot(x2, gauss(x2), 'o')
plt.plot(x, gauss(x))
plt.text(-0.5, 1, 'integration/gauss3.py')
plt.fill_between(x2,gauss(x2))
plt.show()

I = (gauss(x2[0]) + gauss(x2[-1]) + 2*np.sum(gauss(x2[1:-1])))/6
print(I)
