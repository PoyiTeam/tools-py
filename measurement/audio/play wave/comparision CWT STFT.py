#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from scipy.signal import stft
from scipy.fft import fft
import pywt

#%%
num = 1024
cycle = 5
time = np.linspace(start=0, stop=10, num=num)
time = np.linspace(start=0, stop=np.pi*cycle, num=num)
sinwave = np.sin(time) + np.sin(time*0.5)

step = 12
start = 785
mid = start+step
end = mid+step
sinwave[start:mid] = np.linspace(start=sinwave[start], stop=5, num=mid-start)
sinwave[mid:end] = np.linspace(start=5, stop=sinwave[mid], num=end-mid)
sample_rate = 20
period = 1/sample_rate
#%% STFT
window = "hamm"
nperseg = 36
freq, t, stft_spec = stft(sinwave,
                             sample_rate,
                             nperseg=nperseg,
                             noverlap=int(nperseg/3),
                             window=window)
stft_spec = abs(stft_spec)


#%% CWT
width = np.arange(1,31)
coef, freqs = pywt.cwt(sinwave,width,'mexh')

#%%
fontsize = 10
labelsize = 7.5

fig = plt.figure(num=1, clear=True, facecolor="white")
ax = fig.add_subplot(3, 1, 1)
# plt.figure(figsize=(20,8))
ax.set_title("Signal", fontsize = fontsize)

ax.set_xticks([])
ax.set_xlim([0, max(time)])

ax.set_yticks([])
ax.set_ylim([-5, 6])

ax.plot(time,sinwave)

ax.set_ylabel("Amplitude", fontsize=fontsize)

#%%
ax = fig.add_subplot(3, 1, 2)

x, y = np.meshgrid(t, freq)
ax.pcolormesh(x, y, stft_spec, vmin=0, shading="auto", cmap="jet")

ax.set_title("STFT spectrogram", fontsize = fontsize)

ax.set_xticks([])
ax.set_xlim([0, t[-1]])

ax.set_yticks([])
ax.set_ylim([0, max(freq)])

ax.set_ylabel("Frequency", fontsize=fontsize)

#%%
x, y = np.meshgrid(time, freqs)

ax = fig.add_subplot(3, 1, 3)

ax.pcolormesh(x, y, coef, vmin=0, shading="auto", cmap="jet")

ax.set_title("CWT scalogram", fontsize = fontsize)

ax.set_xticks([])
ax.set_xlim([0, time[-1]])

ax.set_yticks([])
ax.set_ylim([0.01, 0.1])

ax.set_xlabel("Time", fontsize=fontsize)
ax.set_ylabel("Frequency", fontsize=fontsize)

plt.show()

#%%
plt.figure(2)
sinwave

sinwave_fft = abs(fft(sinwave))
signal_spectrum = sinwave_fft[0:int(len(sinwave_fft)/2)]
# freqs = np.linspace(0,int(rate/2),len(signal_spectrum))
plt.figure(2)
plt.plot(signal_spectrum,  lw=1)