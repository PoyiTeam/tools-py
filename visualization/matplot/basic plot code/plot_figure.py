#%%
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.axes as axes

#%% create fig
fig = plt.figure(
    figsize=(8, 8),
    dpi=100,
    edgecolor="black",
    facecolor="black",
    linewidth=1,
    frameon=False,
    #subplotpars="figure.subplot.*",
    tight_layout=True,
    constrained_layout=False)
fig.suptitle("figure title")
#%% add subplots
axs = [fig.add_subplot(2, 1, 1), fig.add_subplot(2, 1, 2)]
fig

#%% plot y=x
axes.Axes.clear(axs[0])
x1 = np.arange(0, 10.1, 0.1)
y1 = np.arange(0, 10.1, 0.1)
x2 = np.arange(0, 10.1, 0.1)
y2 = np.arange(10, -0.1, -0.1)

axs[0].set_title("subplot title 0")
axs[0].plot(x1, y1, label="line1", linewidth=2)
axs[0].plot(x2, y2, label="line2", linewidth=8)
axs[0].set_xlim(0, 10)
axs[0].set_ylim(0, 10)
axs[0].set_xticks(np.arange(0, 10.1, 5))
axs[0].set_xlabel("this is x label")
axs[0].set_yticks(np.arange(0, 10.1, 5))
axs[0].set_ylabel("this is y label")
axs[0].legend()
fig

#%% clear specific axis
axes.Axes.clear(axs[0])
fig

#%% hide specific axis
axs[1].axis("off")
fig

#%% clear current axis
plt.cla()

#%% clear entire figure
plt.clf()
fig
