import matplotlib.pyplot as plt
import numpy as np

x = np.array([10, 30, 5])
labels = np.array(['Male', 'Female', 'Others'])

plt.pie(x, labels=labels)

plt.show()