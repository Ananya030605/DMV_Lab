import matplotlib.pyplot as plt


categories = ['A', 'B', 'C', 'D']
values = [23, 45, 12, 37]


plt.bar(categories, values)


plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Static Bar Chart Example')


plt.show()
