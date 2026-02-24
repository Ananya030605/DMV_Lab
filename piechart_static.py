import matplotlib.pyplot as plt

labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [30, 25, 25, 20]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']


plt.figure(figsize=(6,6))
plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%', 
    startangle=90        
)

plt.title('Fruit Distribution')
plt.axis('equal')  

plt.show()
