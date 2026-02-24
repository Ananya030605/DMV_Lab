import matplotlib.pyplot as plt
import numpy as np

plt.ion()
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(-1.5, 1.5)

x = np.arange(100)
y = np.zeros(100)

line, = ax.plot(x, y)

for i in range(300):
    y = np.roll(y, -1)
    y[-1] = np.cos(i * 0.1)
    line.set_ydata(y)
    plt.pause(0.05)

plt.ioff()
plt.show()
