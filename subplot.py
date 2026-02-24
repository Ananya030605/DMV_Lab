import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12000, 15000, 18000, 17000, 20000, 22000]
expenses = [8000, 9000, 10000, 9500, 11000, 12000]

x = np.arange(len(months))

plt.figure(figsize=(8, 5))

plt.bar(x, expenses, width=0.4, label="Expenses", color="orange")
plt.plot(x, sales, marker='o', color="blue", label="Sales")

plt.xticks(x, months)
plt.title("Sales and Expenses Comparison")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()
plt.tight_layout()

plt.show()
