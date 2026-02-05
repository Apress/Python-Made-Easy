import random

n = 100000
inside_circle = 0
random.seed(0)

for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        inside_circle += 1
pi_estimate = (inside_circle / n) * 4
print(pi_estimate) # 3.129