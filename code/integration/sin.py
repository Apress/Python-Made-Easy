import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)

y = 1/abs(np.sin(x))

plt.plot(x, y)

plt.text(0.5, 0.5, 'integration/sin.py')
plt.show()

