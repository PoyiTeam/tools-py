import itertools
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#%%
def data_gen():
    for cnt in itertools.count():
        t = cnt / 20
        yield t, np.sin(2*np.pi*t)
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
    
    if len(xdata) > 220:
        del xdata[0:20]
        del ydata[0:20]

    if t > xmax:
        ax.set_xlim(t-10, t)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)
    
    return line,
#%%
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []

#%%
ani = animation.FuncAnimation(fig, run,
                              frames=data_gen,
                              init_func=init,
                              interval=10)
plt.show()