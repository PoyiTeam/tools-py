#%%
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.fromnumeric import var

data = np.array([10, 9, 4, 3, 2, 3, 4, 9, 10, 8, 8])
x = np.linspace(start=0, stop=len(data) - 1, num=len(data))
y = data
plt.plot(x, y)

# check trough

for i in range(len(data) - 1):
    variance = data[i + 1] - data[i]

    # if variance > 0, return 1 || variance < 0, return -1
    variance_type = np.sign(variance)
    print("num", str(i), ":", variance_type)
    if variance_type == 1:
        print("positive variance")
    elif variance_type == -1:
        print("negative variance")
    else:
        print("no variance")

# %%
