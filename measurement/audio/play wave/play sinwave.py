#%%
import numpy as np
from numpy import pi
from pydub import AudioSegment
from pydub.playback import play
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft
#%%
rate = 44100
sinwave_freq = 500
time = 3

wav = wavfile.read("Dry Guitar amp (no cabinet).wav")
rate, music_signal = wav

music_signal = music_signal[:,0]
start = rate * 5
end = rate * 10
#%%
sinwave_1 = np.sin(np.linspace(0, sinwave_freq*time*pi, rate*time, dtype="float32"))*0.5
# sinwave_2 = np.sin(np.linspace(0, sinwave_freq*0.5*time*pi, rate*time, dtype="float32"))*0.3
# sinwave = sinwave_1 + sinwave_2
# sinwave = sinwave_1
# signal = sinwave
signal = music_signal[start:end]*1
audio_segment = AudioSegment(signal.tobytes(),
                             frame_rate=rate,
                             sample_width=signal.dtype.itemsize,
                             channels=1)
#%%
# plt.plot(signal[0:int(rate/250*5)])
start = rate * 5
end = rate * 10
plt.figure(1)
plt.plot(signal[0:100000], lw=1)
plt.grid()
#%%
play(audio_segment)
#%%
signal_fft = abs(fft(signal))
signal_spectrum = signal_fft[0:int(len(signal_fft)/2)]
freqs = np.linspace(0,int(rate/2),len(signal_spectrum))
plt.figure(2)
plt.plot(freqs, signal_spectrum,  lw=0.1)
plt.grid()