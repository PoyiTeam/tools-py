#%%
import matplotlib.pyplot as plt
import numpy as np

#%% create figure
fig = plt.figure(
    figsize=(8, 4),
    dpi=100,
    edgecolor="black",
    facecolor="black",
    linewidth=1,
    frameon=False,
    #subplotpars="figure.subplot.*",
    tight_layout=True,
    constrained_layout=False)
fig.suptitle("fuzzy set")

axs = [
    fig.add_subplot(1, 1, 1),
]

start = 10
stop = 30
num = 200


# triangle membership
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


# trapezoid membership
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


#%%

x = np.linspace(start=start, stop=stop, num=num)
gap = stop - start
# hot, warm, cold
params = np.array([
    gap * 0.0 + start, gap * 0.0 + start, gap * 0.3 + start, gap * 0.4 + start
])
y1 = trapezoid_membership_functoin(x, params)
params = np.array([
    gap * 0.3 + start, gap * 0.4 + start, gap * 0.6 + start, gap * 0.7 + start
])
y2 = trapezoid_membership_functoin(x, params)
params = np.array(
    [gap * 0.6 + start, gap * 0.7 + start, gap * 1 + start, gap * 1 + start])
y3 = trapezoid_membership_functoin(x, params)

axs_idx = 0
axs[axs_idx].set_title("fuzzy (membership function: trapezoid))")
axs[axs_idx].set_xlim(start, stop)
axs[axs_idx].set_ylim(0, 1.5)
axs[axs_idx].set_xticks(np.linspace(start=start, stop=stop, num=3))
axs[axs_idx].set_xlabel("temperature")
axs[axs_idx].set_yticks(np.linspace(start=0, stop=1, num=3))
axs[axs_idx].set_ylabel("y")

axs[axs_idx].plot(x, y1, label="Cold", linewidth=2, color="blue")
axs[axs_idx].plot(x, y2, label="Warm", linewidth=2, color="orange")
axs[axs_idx].plot(x, y3, label="Hot", linewidth=2, color="red")

axs[axs_idx].legend()
#%%
fig

# #%% trapezoid membership demo
# def trapezoid_membership_functoin(x, params):
#     """
#     params must give 4 values [a, b, c, d]
#     a < b < c < d
#     """
#     a = params[0]
#     b = params[1]
#     c = params[2]
#     d = params[3]

#     y = np.zeros(len(x))
#     for i in range(len(x)):
#         y[i] = max(min((x[i] - a) / (b - a), 1, (d - x[i]) / (d - c)), 0)
#     return y

# x3 = np.linspace(start=start, stop=stop, num=num)
# params = np.array([stop * 0.2, stop * 0.3, stop * 0.5, stop * 0.7])
# y3 = trapezoid_membership_functoin(x3, params)

# axs[2].set_title("fuzzy (membership function: trapezoid))")
# axs[2].plot(x3, y3, label="line", linewidth=2)
# axs[2].set_xlim(0, stop)
# axs[2].set_ylim(0, 1.1)
# axs[2].set_xticks(np.linspace(start=start, stop=stop, num=3))
# axs[2].set_xlabel("this is x label")
# axs[2].set_yticks(np.linspace(start=start, stop=1, num=3))
# axs[2].set_ylabel("this is y label")
# axs[2].legend()

# #%% guassian membership demo
# def guassian_membership_functoin(x, params):
#     """
#     params must give 2 values [sigma, c]
#     sigma: standard deviation
#     c: mean
#     """
#     sigma = params[0]
#     c = params[1]

#     y = np.zeros(len(x))
#     for i in range(len(x)):
#         y[i] = np.exp(-(x[i] - c)**2 / (2 * sigma**2))
#     return y

# x4 = np.linspace(start=start, stop=stop, num=num)
# params = np.array([2, 5])
# y4 = guassian_membership_functoin(x4, params)

# axs[3].set_title("fuzzy (membership function: guassian))")
# axs[3].plot(x4, y4, label="line", linewidth=2)
# axs[3].set_xlim(0, stop)
# axs[3].set_ylim(0, 1.1)
# axs[3].set_xticks(np.linspace(start=start, stop=stop, num=3))
# axs[3].set_xlabel("this is x label")
# axs[3].set_yticks(np.linspace(start=start, stop=1, num=3))
# axs[3].set_ylabel("this is y label")
# axs[3].legend()

# #%%
# #%% guassian membership demo
# def gbell_membership_functoin(x, params):
#     """
#     params must give 2 values [sigma, c]
#     sigma: standard deviation
#     c: mean
#     """
#     a = params[0]
#     b = params[1]
#     c = params[2]

#     y = np.zeros(len(x))
#     for i in range(len(x)):
#         y[i] = 1 / (1 + abs((x[i] - c) / a)**(2 * b))
#     return y

# x5 = np.linspace(start=start, stop=stop, num=num)
# params = np.array([stop * 0.2, stop * 0.4, stop * 0.7])
# y5 = gbell_membership_functoin(x5, params)

# axs.append(fig.add_subplot(3, 2, 5))

# axs[4].set_title("fuzzy (membership function: generalized bell))")
# axs[4].plot(x5, y5, label="line", linewidth=2)
# axs[4].set_xlim(0, stop)
# axs[4].set_ylim(0, 1.1)
# axs[4].set_xticks(np.linspace(start=start, stop=stop, num=3))
# axs[4].set_xlabel("this is x label")
# axs[4].set_yticks(np.linspace(start=start, stop=1, num=3))
# axs[4].set_ylabel("this is y label")
# axs[4].legend()
#%%
fig
# %%
