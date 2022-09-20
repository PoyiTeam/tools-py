#%%
#%matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt
import itertools
from matplotlib.animation import FuncAnimation
from matplotlib import pyplot, transforms
#%% initialization of figure
def init():
    axs[0][0].set_xlim(0, max_time)
    axs[0][0].set_ylim(-2.5, 2.5)
    axs[0][1].set_xlim(-2.5, 2.5)
    axs[0][1].set_ylim(0, max_time)
    axs[1][0].set_xlim(0, max_time)
    axs[1][0].set_ylim(-2.5, 2.5)
    axs[1][1].set_xlim(-2.5, 2.5)
    axs[1][1].set_ylim(-2.5, 2.5)
    
#%% change x xtrick range and draw vector
def modifyXtrick(ax, x_vals, y_vals, line):
    
    x_vals = np.delete(x_vals,0)
    y_vals = np.delete(y_vals,0)
    
    xmin, xmax = ax.get_xlim()
    
    if x_vals[-1] > xmax:
        ax.set_xlim(x_vals[0], x_vals[-1])
    
    ax.patches = []
    ax.arrow(x_vals[points_half[0]], 0 , 0, y_vals[points_half[0]], color="red")
    line.set_data(x_vals, y_vals)
    line.set_marker("o")
    line.set_markerfacecolor("red")
    line.set_markevery(list(points_half))
    
    return x_vals, y_vals

#%%
def updateFig(i):
    period = next(counter)
    
    # generate signal
    phi_0 = signal_per_second*period
    euler_real_0 = np.cos(phi_0)
    euler_imag_0 = np.sin(phi_0)
    signal_0 = np.sin(phi_0)
    
    phi_1 = signal_per_second*2*period
    euler_real_1 = np.cos(phi_1)
    euler_imag_1 = np.sin(phi_1)
    signal_1 = np.sin(phi_1)

    # signal = signal_0
    # euler_real = euler_real_0
    # euler_imag = euler_imag_0
    
    signal = signal_0 + signal_1
    euler_real = euler_real_0 + euler_real_1
    euler_imag = euler_imag_0 + euler_imag_1
    
    # data to fig
    global x_vals_00, y_vals_00, \
           x_vals_01, y_vals_01, \
           x_vals_10, y_vals_10, \
           x_vals_11, y_vals_11
    
    if i == 0:
        x_vals_00 = np.array([period])
        y_vals_00 = np.array([signal])
        x_vals_01 = np.array([euler_real])
        y_vals_01 = np.array([period])
        x_vals_10 = np.array([period])
        y_vals_10 = np.array([euler_imag])
        x_vals_11 = np.array([euler_real])
        y_vals_11 = np.array([euler_imag])
        
    elif i < points :
        x_vals_00 = np.append(x_vals_00, period)
        y_vals_00 = np.append(y_vals_00, signal)
        x_vals_01 = np.append(x_vals_01, euler_real)
        y_vals_01 = np.append(y_vals_01, period)
        x_vals_10 = np.append(x_vals_10, period)
        y_vals_10 = np.append(y_vals_10, euler_imag)
        x_vals_11 = np.append(x_vals_11, euler_real)
        y_vals_11 = np.append(y_vals_11, euler_imag)
        line_00.set_data(x_vals_00, y_vals_00)
        line_01.set_data(x_vals_01, y_vals_01)
        line_10.set_data(x_vals_10, y_vals_10)
        line_11.set_data(x_vals_11, y_vals_11)
    else:    
        x_vals_00 = np.append(x_vals_00, period)
        y_vals_00 = np.append(y_vals_00, signal)
        x_vals_00, y_vals_00 = modifyXtrick(axs[0][0], x_vals_00, y_vals_00, line_00)
    
        x_vals_01 = np.append(x_vals_01, euler_real)
        y_vals_01 = np.append(y_vals_01, period)
        x_vals_01 = np.delete(x_vals_01,0)
        y_vals_01 = np.delete(y_vals_01,0)
        ymin_01, ymax_01 = axs[0][1].get_ylim()
        if y_vals_01[-1] > ymax_01:
            axs[0][1].set_ylim(y_vals_01[0], y_vals_01[-1])
        axs[0][1].patches = []
        axs[0][1].arrow(0, y_vals_01[points_half[0]], x_vals_01[points_half[0]], 0, color="red")
        line_01.set_data(x_vals_01, y_vals_01)
        line_01.set_marker("o")
        line_01.set_markerfacecolor("red")
        line_01.set_markevery(list(points_half))
        
        x_vals_10 = np.append(x_vals_10, period)
        y_vals_10 = np.append(y_vals_10, euler_imag)
        x_vals_10, y_vals_10 = modifyXtrick(axs[1][0], x_vals_10, y_vals_10, line_10)
        
        x_vals_11 = np.append(x_vals_11, euler_real)
        y_vals_11 = np.append(y_vals_11, euler_imag)
        x_vals_11 = np.delete(x_vals_11, 0)
        y_vals_11 = np.delete(y_vals_11, 0)
        axs[1][1].patches = []
        axs[1][1].arrow(0, 0, euler_real, euler_imag, color="red",
                        head_width=0.05,head_length=0.1,overhang=-0.5,length_includes_head=True)
    
#%% set basic paramters
freq = 2
max_time = 1
sampling_rate = 100
time_step = 1/sampling_rate
points = sampling_rate * max_time
points_half = np.array([int(points/2)-1])
time_line = np.linspace(0, max_time, points)
signal_per_second = 2*np.pi*freq
counter = itertools.count(0, 1/sampling_rate)

#%% set figure properties
fig, axs = plt.subplots(2,2,figsize=(9.5,9.5))
fig.suptitle("Signal and Euler equation", fontsize=16)

# grid on
for ax in axs:
    for _ax in ax:
        _ax.grid()

line_00, = axs[0][0].plot([], [], lw=1.5)
line_01, = axs[0][1].plot([], [], lw=1.5)
line_10, = axs[1][0].plot([], [], lw=1.5)
line_11, = axs[1][1].plot([], [], lw=1.5)

axs[0][0].set_title("Raw signal")
axs[0][0].set_xlabel("Time(s)")
axs[0][0].set_ylabel("Amplitude")
axs[0][1].set_title("Euler's equation - Real")
axs[0][1].set_xlabel("Real Quantity")
axs[0][1].set_ylabel("Time(s)")
axs[1][0].set_title("Euler's equation - Imaginary")
axs[1][0].set_xlabel("Time(s)")
axs[1][0].set_ylabel("Imaginary Quantity")
axs[1][1].set_title("Euler's equation")
axs[1][1].set_xlabel("Real")
axs[1][1].set_ylabel("Imaginary")

#%% animate
# frame=30*10
ani = FuncAnimation(fig, updateFig,
                    init_func=init,
                    # frames=frame,
                    interval=10,
                    blit=False)
fig.tight_layout()

# ani_name = 'signal to euler - mix sinwave.gif'
# ani.save(ani_name, fps=30, dpi=60)
plt.show()