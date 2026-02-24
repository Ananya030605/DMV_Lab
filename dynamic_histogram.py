import matplotlib.pyplot as plt
import numpy as np
from collections import deque

plt.ion()
fig, ax = plt.subplots()

data = deque(maxlen=200)

for _ in range(400):
    data.append(np.random.randn())
    ax.clear()
    ax.hist(data, bins=20, color='blue', edgecolor='black')
    ax.set_xlim(-4, 4)
    ax.set_ylim(0, 40)
    plt.pause(0.05)

plt.ioff()
plt.show()
