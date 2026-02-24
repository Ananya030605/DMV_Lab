import matplotlib.pyplot as plt

# Data
data = [12, 15, 14, 10, 18, 20, 22, 17, 16, 19, 21]

# Plot histogram
plt.hist(data, bins=5)

# Labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Static Histogram')

# Show plot
plt.show()
