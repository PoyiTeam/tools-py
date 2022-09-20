import numpy as np
import matplotlib.pyplot as plt


def multiple_img_plot(key, data, rows, cols):
    """
    title: string
        dictionary key
    data:
        dictionary, 2D plot data
    """

    plt.clf()
    fig, ax = plt.subplots(figsize=(25, 15), nrows=rows, ncols=cols)
    fig.suptitle(key)
    ytick_num = 5
    for idx, title in enumerate(data):

        ax.ravel()[idx].set_title(key)
        ax.ravel()[idx].set_xlabel("points")
        ax.ravel()[idx].set_ylabel("frequency(Hz)")
        ax.ravel()[idx].set_xlim([-200, 0])
        ax.ravel()[idx].set_ylim([0, 1000])
        ax.ravel()[idx].yaxis.tick_right()
        # ax.ravel()[idx].yaxis.set_ticklabels([])
        ax.ravel()[idx].tick_params(axis='y', labelrotation=90)
        ax.ravel()[idx].locator_params(axis="y", nbins=20)
        # ax.ravel()[idx].set_xticks(x_pos_arr, time_arr)
        # ax.ravel()[idx].set_xticks(time_arr)
        # ax.ravel()[idx].set_yticks([])
        # ax.ravel()[idx].pcolormesh(spectrograms[key], cmap="jet")
        ax.ravel()[idx].imshow(data[key],  interpolation="nearest",
                               aspect="auto", cmap="jet", origin="lower")

    # fig.tight_layout()
    plt.show()
    return fig, ax
