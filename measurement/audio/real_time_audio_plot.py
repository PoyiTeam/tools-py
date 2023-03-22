# %%
import sounddevice as sd
import numpy as np
import queue
import sys
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import argparse

parser = argparse.ArgumentParser(add_help=False)
# %%
fs = 48000
channels = [1]
window = 100  # visible time slot (ms)
downsample = 20  # down sampling ratio (greater than 1)
block_duration = 100  # interval of each chunck (ms)
chunk = int(fs * block_duration / 1000)  # chunck size
device = sd.default.device
mapping = [c - 1 for c in (channels)]  # Channel numbers start with 1
q = queue.Queue()
print(f'default device num: {device}')
# %%


def audio_callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)

    # Fancy indexing with mapping creates a (necessary!) copy:
    print("chunk size: {}".format(indata.shape))
    print("down sample size: {}".format(indata[downsample - 1, mapping].shape))
    q.put(indata[::downsample, mapping])


def update_plot(frame):
    """This is called by matplotlib for each plot update.

    Typically, audio callbacks happen more frequently than plot updates,
    therefore the queue tends to contain multiple blocks of audio data.

    """
    global plotdata

    while True:
        try:
            data = q.get_nowait()
        except queue.Empty:
            break
        shift = len(data)
        plotdata = np.roll(plotdata, -shift, axis=0)
        plotdata[-shift:, :] = data
    for column, line in enumerate(lines):
        line.set_ydata(plotdata[:, column])
    return lines


# %%
try:
    if fs is None:
        device_info = sd.query_devices(device, "input")
        fs = device_info["default_samplerate"]

    length = int(window * fs / (1000 * downsample))
    plotdata = np.zeros((length, len(channels)))

    fig, ax = plt.subplots()
    lines = ax.plot(plotdata)
    if len(channels) > 1:
        ax.legend(
            ["channel {}".format(c) for c in channels],
            loc="lower left",
            ncol=len(channels),
        )
    ax.axis((0, len(plotdata), -1, 1))
    ax.set_yticks([0])
    ax.yaxis.grid(True)
    ax.tick_params(
        bottom=False,
        top=False,
        labelbottom=False,
        right=False,
        left=False,
        labelleft=False,
    )
    fig.tight_layout(pad=0)

    stream = sd.InputStream(
        device=device,
        channels=max(channels),
        samplerate=fs,
        callback=audio_callback,
        blocksize=chunk,
    )
    ani = FuncAnimation(fig, update_plot, interval=100, blit=True)
    with stream:
        plt.show()
except Exception as e:
    pass
    # parser.exit(type(e).__name__ + ": " + str(e))
