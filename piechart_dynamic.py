import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [25, 25, 25, 25]

fig, ax = plt.subplots()

def update(frame):
    ax.clear()  
    

    new_sizes = [random.randint(10, 40) for _ in sizes]
    
    ax.pie(
        new_sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90
    )
    
    ax.set_title("Dynamic Pie Chart (Updating Every Second)")
    ax.axis('equal')  


ani = animation.FuncAnimation(fig, update, interval=1000)

plt.show()
