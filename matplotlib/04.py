import matplotlib.pyplot as plt

x = [5, 10, 15, 20, 25 ]
y = [55, 103, 130, 150, 170]

x1=[30, 35, 40, 45, 50]
y1=[190, 210, 230, 250, 270]

plt.subplot(2, 1, 1)
plt.plot(x, y, 'b', linestyle='solid',  marker='o', markersize=5, mec='r', mfc="y")

plt.title("Scrore over by over \n India vs Australia", fontdict = { 'color': 'red', 'style': 'italic', 'size': 10 }, loc="left")

plt.xlabel("Overs",  fontdict = { 'color': 'green', 'style': 'italic', 'size': 10 })
plt.ylabel("Runs",  fontdict = { 'color': 'pink', 'style': 'italic', 'size': 10 })
plt.grid(color="gray", linestyle="--", linewidth=0.5)



plt.subplot(2, 1, 2)
plt.plot(x1, y1, 'b', linestyle='solid',  marker='o', markersize=5, mec='r', mfc="y")

plt.title("Scrore over by over \n India vs Australia", fontdict = { 'color': 'red', 'style': 'italic', 'size': 10 }, loc="left")

plt.xlabel("Overs",  fontdict = { 'color': 'green', 'style': 'italic', 'size': 10 })
plt.ylabel("Runs",  fontdict = { 'color': 'pink', 'style': 'italic', 'size': 10 })
plt.grid(color="gray", linestyle="--", linewidth=0.5)

plt.show()