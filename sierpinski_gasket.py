import matplotlib.pyplot as plt
import numpy as np
import time

startTime = time.perf_counter()
point_lst = []

for y in range(0,256):
    for x in range(0, 256):
        if (x & (y-x)) == 0: 
            point_lst.append([x+128-.5*y, 256-y]) # replacing y with 256-y will flip the image, since with y it is 
                                                  # upside-down

for p in point_lst:
    plt.scatter(p[0], p[1], s=1, c='black', marker='s')

plt.show()
# line 19 is not working for some reason
plt.close('all')

endTime = time.perf_counter()
print("Execution Time", (endTime - startTime)/60)