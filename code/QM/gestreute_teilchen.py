# scattering potential
a = 1
V_0 = 1
E = 0.1
dx = 0.05

def V(x):
    if x < -a or x > a:
        return 0
    return V_0

def k(E, x):
    return E - V(x)

def phi_numerov(E, dx, x, phi):
    c = 1+(dx**2/12)*k(E, x+dx)
    d = 2*(1-5*(dx**2/12)*k(E, x))*phi[-1] - (1+(dx**2/12)*k(E, x-dx))*phi[-2]
    return d/c

phi = []
x = []
phi.append(1)
x.append(-dx/2)
phi.append(1)
x.append(dx/2)

for i in range(1000):
    x.append(x[-1]+dx)
    phi.append(phi_numerov(E, dx, x[-1], phi))

import matplotlib.pyplot as plt
plt.plot(x, phi)
plt.show()
