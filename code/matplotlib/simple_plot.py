import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 12})

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.savefig('images/simple_plot.png')