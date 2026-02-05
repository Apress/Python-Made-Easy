import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 12})

x = np.linspace(-5, 5, 100)

def gauss(x):
    return np.exp(-x**2)
y = gauss(x)

x2 = np.linspace(-1, 0, 10)

plt.plot(x, gauss(x))
plt.plot(x, 0*x, color="black")
plt.fill_between(x2,gauss(x2))
plt.xlabel('x')
plt.ylabel('y')

# plt.show()
plt.savefig('images/integration.png', bbox_inches='tight')

