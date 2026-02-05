import math
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 12})

x_0 = 20
v_0 = 0
dt = 0.3

v = [v_0]
x = [x_0]

t = [i for i in range(100)]

def a(x):
	if x < 0:
		return 0.01*x**3
	else:
		return 0

for _ in t:
	v.append(v[-1] - 10*dt - a(x[-1])*dt)
	x.append(x[-1] + v[-1]*dt)


plt.plot(t, x[:-1])
plt.show()