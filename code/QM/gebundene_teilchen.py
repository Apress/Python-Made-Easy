import matplotlib.pyplot as plt

# scattering potential
a = 1
V_0 = -1
E = -0.45
dx = 0.01

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


def calculate_waveform(E):
    phi = []
    x = []
    phi.append(1)
    x.append(-dx/2)
    phi.append(1)
    x.append(dx/2)

    for _ in range(1000):
        x.append(x[-1]+dx)
        phi.append(phi_numerov(E, dx, x[-1], phi))

    plt.plot(x, phi)
    plt.show()
    return phi[-1]

E = [-0.4, -0.5]
phi = []
phi.append(calculate_waveform(E[0]))
phi.append(calculate_waveform(E[1]))

while abs(phi[-1]) > 0.1:
    E_neu = E[-1] - phi[-1] * (E[-1] - E[-2]) / (phi[-1] - phi[-2])
    phi.append(calculate_waveform(E_neu))
    E.append(E_neu)


