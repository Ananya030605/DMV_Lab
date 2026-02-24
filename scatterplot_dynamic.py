import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_title("Dynamic Scatter Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

scat = ax.scatter([], [])

x_data = []
y_data = []

def update(frame):
    x_data.append(random.uniform(0, 10))
    y_data.append(random.uniform(0, 10))
    
    scat.set_offsets(list(zip(x_data, y_data)))
    return scat,

ani = animation.FuncAnimation(fig, update, interval=500)

plt.show()
