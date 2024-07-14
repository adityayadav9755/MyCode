import numpy as np
import matplotlib.pyplot as plt

names = ["A", "B", "C"]
phy = [1, 2, 3]
chem = [4, 5, 6]
maths = [7, 8, 9]

x = np.arange(len(names))
w = 0.2

plt.bar(x, phy, width=w)
plt.bar(x+w, chem, width=w)
plt.bar(x+w+w, maths, width=w)
plt.xticks(x+w, names)
plt.show()
