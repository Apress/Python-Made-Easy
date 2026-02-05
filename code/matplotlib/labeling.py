import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size': 12})

t = np.linspace(0,10,100)
y = np.sin(t)
plt.plot(t, y, label='y=sin(t)')
plt.xlabel("t [s]")
plt.ylabel("y [m]")
plt.legend()
plt.savefig('images/labeling.png', bbox_inches='tight')