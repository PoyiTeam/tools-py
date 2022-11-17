import queue
import numpy as np
import sounddevice as sd


class AudioRecorder:
    def __init__(self, fs, window, channels):
        self.name = "audio recorder"
        self.fs = fs
        self.channels = channels  # specific channel list
        self.window = window    # interval of each frame (ms)
        self.frame_size = int(self.fs * self.window * 0.001)
        self.trigger = False
        self.downsample = 1  # down sampling ratio (greater than 1)
        # self.input_device = sd.default.device
        self.input_device = 2
        # mapping channel index
        self.mapping = [c - 1 for c in (self.channels)]
        self.max_qsize = 20
        self.queue_plot_data = queue.Queue(maxsize=self.max_qsize)
        self.queue_raw_data = queue.Queue(maxsize=self.max_qsize)
        self.stream = sd.InputStream(
            device=self.input_device,
            channels=max(self.channels),
            samplerate=self.fs,
            callback=self.audio_callback,
            blocksize=self.frame_size,
            latency="low",
        )
        self.pa_ref = 0.00002  # pa ref

        self.plot_len = int(self.frame_size / self.downsample)

    def audio_callback(self, indata, frames, time, status):

        # print("doing audio callback, chunk length:", len(indata))
        # print("print part of input data:", indata[0], indata[1])
        self.queue_plot_data.put(np.squeeze(
            indata[:: self.downsample, self.mapping]))
        self.queue_raw_data.put(np.squeeze(indata[:, self.mapping]))
        print("recording")

    def start_streaming(self):
        print("doing start_streaming Function")
        self.stream.start()
        print("stream active:", self.stream.active)

    def stop_streaming(self):
        print("doing stop_streaming Function")
        self.stream.stop()
        print("stream active:", self.stream.active)
