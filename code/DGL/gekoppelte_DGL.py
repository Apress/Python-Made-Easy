import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 12})


B = [10]
R = [11]

for i in range(1000):
    B.append(B[i] + 0.01 * B[i] - 0.001 * R[i]*B[i])
    R.append(R[i] -0.1 * R[i] + 0.01 * R[i]*B[i])

plt.plot(B, label='Beute')
plt.plot(R, label='Räuber')
plt.show()