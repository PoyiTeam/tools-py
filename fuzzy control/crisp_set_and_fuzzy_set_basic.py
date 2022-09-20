#%%
import matplotlib.pyplot as plt
import numpy as np

#%% create figure
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
fig.suptitle("crisp vs fuzzy")

axs = [
    fig.add_subplot(3, 2, 1),
    fig.add_subplot(3, 2, 2),
    fig.add_subplot(3, 2, 3),
    fig.add_subplot(3, 2, 4)
]

start = 0
stop = 10
num = 200
#%% crisp sets
x1 = np.linspace(start=start, stop=stop, num=num)
y1 = np.linspace(start=start, stop=1, num=num)

i = 0
threshold = 0.5

low_values_idx = y1 < threshold
high_values_idx = y1 > threshold
y1[low_values_idx] = 0
y1[high_values_idx] = threshold

axs[0].set_title("crisp")
axs[0].plot(x1, y1, label="line", linewidth=2)
axs[0].set_xlim(0, stop)
axs[0].set_ylim(0, 1.1)
axs[0].set_xticks(np.linspace(start=start, stop=stop, num=3))
axs[0].set_xlabel("this is x label")
axs[0].set_yticks(np.linspace(start=start, stop=1, num=3))
axs[0].set_ylabel("this is y label")
axs[0].legend()


#%% triangle membership demo
def triangle_membership_function(x, params):
    """
    params must give 3 values [a, b, c]
    a < b < c
    """
    a = params[0]
    b = params[1]
    c = params[2]

    y = np.zeros(len(x))
    for i in range(len(x)):
        y[i] = max(min((x[i] - a) / (b - a), (c - x[i]) / (c - b)), 0)
    return y


#x2 = np.linspace(start=start, stop=stop, num=num)
x2 = np.linspace(start=start, stop=stop, num=num)
params = np.array([stop * 0.2, stop * 0.5, stop * 0.7])
y2 = triangle_membership_function(x2, params)

axs[1].set_title("fuzzy (membership function: triangle))")
axs[1].plot(x2, y2, label="line", linewidth=2)
axs[1].set_xlim(0, stop)
axs[1].set_ylim(0, 1.1)
axs[1].set_xticks(np.linspace(start=start, stop=stop, num=3))
axs[1].set_xlabel("this is x label")
axs[1].set_yticks(np.linspace(start=start, stop=1, num=3))
axs[1].set_ylabel("this is y label")
axs[1].legend()


#%% trapezoid membership demo
def trapezoid_membership_functoin(x, params):
    """
    params must give 4 values [a, b, c, d]
    a < b < c < d
    """
    a = params[0]
    b = params[1]
    c = params[2]
    d = params[3]

    y = np.zeros(len(x))
    for i in range(len(x)):
        y[i] = max(min((x[i] - a) / (b - a), 1, (d - x[i]) / (d - c)), 0)
    return y


x3 = np.linspace(start=start, stop=stop, num=num)
params = np.array([stop * 0.2, stop * 0.3, stop * 0.5, stop * 0.7])
y3 = trapezoid_membership_functoin(x3, params)

axs[2].set_title("fuzzy (membership function: trapezoid))")
axs[2].plot(x3, y3, label="line", linewidth=2)
axs[2].set_xlim(0, stop)
axs[2].set_ylim(0, 1.1)
axs[2].set_xticks(np.linspace(start=start, stop=stop, num=3))
axs[2].set_xlabel("this is x label")
axs[2].set_yticks(np.linspace(start=start, stop=1, num=3))
axs[2].set_ylabel("this is y label")
axs[2].legend()


#%% guassian membership demo
def guassian_membership_functoin(x, params):
    """
    params must give 2 values [sigma, c]
    sigma: standard deviation
    c: mean
    """
    sigma = params[0]
    c = params[1]

    y = np.zeros(len(x))
    for i in range(len(x)):
        y[i] = np.exp(-(x[i] - c)**2 / (2 * sigma**2))
    return y


x4 = np.linspace(start=start, stop=stop, num=num)
params = np.array([2, 5])
y4 = guassian_membership_functoin(x4, params)

axs[3].set_title("fuzzy (membership function: guassian))")
axs[3].plot(x4, y4, label="line", linewidth=2)
axs[3].set_xlim(0, stop)
axs[3].set_ylim(0, 1.1)
axs[3].set_xticks(np.linspace(start=start, stop=stop, num=3))
axs[3].set_xlabel("this is x label")
axs[3].set_yticks(np.linspace(start=start, stop=1, num=3))
axs[3].set_ylabel("this is y label")
axs[3].legend()


#%%
#%% guassian membership demo
def gbell_membership_functoin(x, params):
    """
    params must give 2 values [sigma, c]
    sigma: standard deviation
    c: mean
    """
    a = params[0]
    b = params[1]
    c = params[2]

    y = np.zeros(len(x))
    for i in range(len(x)):
        y[i] = 1 / (1 + abs((x[i] - c) / a)**(2 * b))
    return y


x5 = np.linspace(start=start, stop=stop, num=num)
params = np.array([stop * 0.2, stop * 0.4, stop * 0.7])
y5 = gbell_membership_functoin(x5, params)

axs.append(fig.add_subplot(3, 2, 5))

axs[4].set_title("fuzzy (membership function: generalized bell))")
axs[4].plot(x5, y5, label="line", linewidth=2)
axs[4].set_xlim(0, stop)
axs[4].set_ylim(0, 1.1)
axs[4].set_xticks(np.linspace(start=start, stop=stop, num=3))
axs[4].set_xlabel("this is x label")
axs[4].set_yticks(np.linspace(start=start, stop=1, num=3))
axs[4].set_ylabel("this is y label")
axs[4].legend()
#%%
fig
# %%
