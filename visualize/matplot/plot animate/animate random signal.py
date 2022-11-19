import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#%%
def init():
    ax.set_ylim(-5, 5)
    ax.set_xlim(0, 1)
    del x_vals[:]
    del y_vals[:]
    line.set_data(x_vals, y_vals)
    
    return line

#%%
def func(i):
    time_trough = np.floor((time.time() - start_time)*100)/100
    x_vals.append(time_trough)
    y_vals.append(np.random.randint(-4, 5))
    
    xmin, xmax = ax.get_xlim()
    if len(x_vals) > 100:
        del x_vals[0]
        del y_vals[0]

    if x_vals[-1] > xmax:
        ax.set_xlim(x_vals[0], x_vals[-1])
        ax.figure.canvas.draw()
    line.set_data(x_vals, y_vals)
    
    return line

#%%
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
x_vals, y_vals = [], []
start_time = time.time()

#%%
time_step = 25 # (ms)

ani = FuncAnimation(fig, func,
                    init_func=init,
                    interval=time_step,
                    blit=False)
plt.show()