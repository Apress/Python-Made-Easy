import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 0, 100)

x2 = np.linspace(-1, 0, 4)
x2_durchschnitt = (x2[1:]+ x2[:-1])/2

def gauss(x):
    return np.exp(-x**2)

plt.plot(x, gauss(x))
plt.plot(x2_durchschnitt, gauss(x2_durchschnitt), 'o')
plt.plot(x, 0*x)
plt.bar(x2_durchschnitt, gauss(x2_durchschnitt), width = 0.333)
plt.text(-0.5, 1, 'integration/gauss2.py')
plt.show()

I = sum(gauss(x2_durchschnitt)*0.333)
print(I)
