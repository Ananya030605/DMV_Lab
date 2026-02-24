import matplotlib.pyplot as plt
n = int(input("Enter number of bars:"))
labels = []
values = []
for i in range(n):
    label = input(f"Enter label for bar {i+1}:")
    value = int(input(f"Enter value for bar {i+1}:"))
    labels.append(label)
    values.append(value)
plt.bar(labels, values)
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Dynamic Bar Chart (User Input)")
plt.show()    