import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 1, 5, 7, 3]

plt.figure(figsize=(6, 4))
plt.scatter(x, y, color='blue', marker='o')

plt.title('Static Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.grid(True)

plt.show()
