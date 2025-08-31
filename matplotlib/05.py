import matplotlib.pyplot as plt

x = [2, 5, 6, 8, 4, 3]

y = [3, 7, 2, 4, 8, 9]

color= ['red', 'blue', 'green', 'yellow', 'purple', 'orange']

sizes = [100, 200, 300, 400, 500, 600]

plt.scatter(x, y, s=sizes, c=color, alpha= 0.6)
# plt.grid()
plt.colorbar()
plt.show()
