import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.optimize import curve_fit

plt.rcParams.update({'font.size': 12})

random.seed(0)
t = np.linspace(0, 5, 20)
s_0 = 10
v_0 = 20
a = -9.81

def f(t, s_0, v_0, a):
    return s_0 + v_0*t + 1/2*a*t**2
y = [f(i, s_0, v_0, a) + random.gauss(0, 2) for i in t]

popt, pcov = curve_fit(f, t, y, p0=[10, 20, -10])

plt.plot(t, y, 'o')
plt.plot(t, f(t, *popt))
plt.xlabel('time [s]')
plt.ylabel('distance [m]')
plt.legend(['Data', f'fit, y(t)={popt[0]:.2f}m+{popt[1]:.2f}m/s*t+1/2*{popt[2]:.2f}m/s^2*t**2'])

plt.savefig('images/curve_fitting_data.png', bbox_inches='tight')