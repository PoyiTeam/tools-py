#%%
import numpy as np
import matplotlib.pyplot as plt
import time
#%%

x = np.linspace(start=0, stop=2*np.pi, num=100)
y = np.sin(x)

plt.plot(x,y)
