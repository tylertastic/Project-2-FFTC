import matplotlib.pyplot as plt
import numpy as np

point_lst = []

for y in range(0,256):
    for x in range(0, 256):
        if (x & y) == 0:
            point_lst.append([x, y])

for p in point_lst:
    plt.scatter(p[0], p[1], s=1, c='black', marker='s')

plt.show()
