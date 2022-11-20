import itertools
import numpy as np
# import matplotlib
# matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# import time

#%%
def data_gen():
    x, y = 0, 0
    count = 100
    for i in range(count):
        x, y = yield x, y
        x += 1
        y += 2
#%%
def init():
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 10)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    
    return line,

#%%
def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()
    # xmin = min(xdata)
    # xmax = max(xdata)
    
    if len(xdata) > 120:
        del xdata[0:20]
        del ydata[0:20]

    if t > xmax:
        ax.set_xlim(t-10, t)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)
    
    return line,

#%% figure setting
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []
#%%
g = data_gen()
x_lst = (i for i in range(10))
y_lst = (i for i in range(0,20,2))
ani = animation.FuncAnimation(fig, run,
                              frames=g,
                              init_func=init(),
                              fargs=1,
                              interval=10)
plt.show()