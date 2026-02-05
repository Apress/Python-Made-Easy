import matplotlib.pyplot as plt
import math

x_0 = 1
v_0 = 0
k = 1
dt = 1

v = [v_0]
x = [x_0]

t = [i for i in range(50)]

for _ in t:
	v.append(v[-1] - k*x[-1]*dt)
	x.append(x[-1] + v[-1]*dt)


x_theorie = [x_0*math.cos(i) for i in t]

plt.plot(t, x[:-1])
plt.plot(t, x_theorie)
plt.title("Oscillator")
plt.xlabel("t[s]")
plt.ylabel("x[m]")

plt.show()