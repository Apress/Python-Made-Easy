import numpy as np

def gauss(x):
    return np.exp(-x**2)

n = 4
a = -1
b = 0

x = np.linspace(a, b, n)
x_support = (x[1:] + x[:-1]) / 2

width = (b-a) / (n-1)
height = gauss(x_support)

I = width * np.sum(height)
print(I)
