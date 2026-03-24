import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(50)
y = -x + np.random.normal(0, 0.1, 50)

x_cluster = np.random.normal(0.8, 0.05, 20)
y_cluster = np.random.normal(0.2, 0.05, 20)

x = np.concatenate([x, x_cluster])
y = np.concatenate([y, y_cluster])

x = np.append(x, 0.2)
y = np.append(y, 2)

plt.figure(figsize=(6,5))
plt.scatter(x, y)

plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot with Negative Correlation, Cluster & Outlier")

plt.show()