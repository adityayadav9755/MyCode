import matplotlib.pyplot as plt

xgraph = []
ygraph = []


def func(x):
    y = x**2 - 128*x + 3007
    return y


for a in range(0, 100):
    xgraph.append(a)
    ygraph.append(func(a))


plt.plot(xgraph, ygraph)
plt.show()
