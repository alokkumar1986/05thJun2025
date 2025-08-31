import matplotlib.pyplot as plt

x = [2, 5, 6, 8, 4, 3]

y = [3, 7, 2, 4, 8, 9]

# plt.bar(x, y, width=0.5)

plt.barh(x, y, height=0.5, color='cyan')

plt.show()