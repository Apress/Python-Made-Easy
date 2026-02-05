import random
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 12})

random.seed(1)

mu = 100
sigma = 50
nums = [random.gauss(mu, sigma) for _ in range(1000)]

plt.hist(nums, bins=10)
plt.xlabel('Value')
plt.ylabel('Number of occurrences')
plt.savefig('images/histogramm.png', bbox_inches='tight')