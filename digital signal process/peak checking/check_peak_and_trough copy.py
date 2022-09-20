#%%
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.fromnumeric import var

data = np.array([[10, 9, 4, 3, 2, 3, 4, 9, 10, 8, 8],
                 [10, 9, 4, 3, 2, 1, 3, 4, 9, 10, 8],
                 [10, 9, 4, 3, 1, 2, 3, 4, 9, 10, 8]])
x = np.linspace(start=0, stop=len(data[0]) - 1, num=len(data[0]))
y1 = data[0]
y2 = data[1]
y3 = data[2]
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

# check trough

lst = []
for element in data:
    i = 0
    variance_type = -1
    while variance_type == -1:
        variance = element[i + 1] - element[i]

        # if variance > 0, return 1 || variance < 0, return -1
        variance_type = np.sign(variance)
        i += 1
    lst.append(i)
    print(lst)
# %%
