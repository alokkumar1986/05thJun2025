import matplotlib.pyplot as plt

x = [2, 5, 6, 8, 4, 3]

y = [3, 7, 2, 4, 8, 9]

color= ['red', 'blue', 'green', 'yellow', 'purple', 'orange']

size = [100, 200, 300, 400, 500, 600]

plt.scatter(x, y, color=color, s=size, alpha=0.5)
plt.grid()
plt.show()
