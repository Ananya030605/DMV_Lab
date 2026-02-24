import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)

x = np.linspace(0, 10, 200)
y = np.sin(x)

line, = ax.plot([], [], lw=2)

def update(frame):
    line.set_data(x[:frame], y[:frame])
    return line,

ani = FuncAnimation(fig, update, frames=len(x), interval=30)
plt.show()
