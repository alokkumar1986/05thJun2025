import matplotlib.pyplot as plt

# from matplotlib import pyplot as plt

x = [0, 2, 4, 6]
y = [1, 3, 5, 7]

plt.plot(x, y, 'hotpink', marker="*", ms=20, linewidth=5, linestyle=":" , mec="blue", mfc="yellow")
plt.grid(color="green", linestyle="dotted", linewidth=2)
plt.show()
