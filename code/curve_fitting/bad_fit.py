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

popt, pcov = curve_fit(f, t, y, p0=[0, 0, 0])

plt.plot(t, y, 'o')
plt.plot(t, f(t, 15, 0, 0))
plt.xlabel('time [s]')
plt.ylabel('distance [m]')
plt.legend(['Data', f'fit, y(t)=15m+0m/s*t+1/2*0m/s^2*t**2'])

# plt.show()
plt.savefig('images/bad_fit.png', bbox_inches='tight')