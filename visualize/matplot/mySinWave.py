#%% import module
import matplotlib.pyplot as plt
import numpy as np
import scipy.fft as fft

#%% simulate sin wave
max_time = 3        # max time, unit: second
sampling_rate = 120   # sampling rate, unit: Hz
num = max_time*sampling_rate
omega = np.linspace(start=0, stop=2*np.pi, num=num)  # radius
time_line = np.linspace(start=0, stop=max_time, num=num)  # time line

# make sin wave
sin_wave_1 = np.sin(1*omega*max_time)   # sin wave 1, 1Hz
sin_wave_2 = np.sin(2*omega*max_time)   # sin wave 2, 2Hz
sin_wave_3 = np.sin(10*omega*max_time)  # sin wave 3, 10Hz
sin_wave_4 = np.sin(30*omega*max_time)  # sin wave 4, 30Hz

# output signal
signal = sin_wave_1 + sin_wave_2 + sin_wave_3 + sin_wave_4

# prepare spectrum params
max_freq = sampling_rate/2     # max frequency is half of the sampling rate
max_point = int(len(signal)/2)      
freqs = np.linspace(start=0, stop=max_freq, num=max_point)    # make frequency axis
signal_fft = fft.fft(signal)
signal_spectrum = abs(signal_fft)

# normalized the value of spectrum from 0 to 1
normalized_spectrum = (signal_spectrum[:]-min(signal_spectrum))/(max(signal_spectrum)-min(signal_spectrum))

#%% plot signal and spectrum

# plot signal
fig, ax = plt.subplots(2, 1,figsize=(10,8))

ax[0].grid()
ax[0].set_xlim(left=0, right=max_time)
ax[0].set_ylim(bottom=-4, top=4)
ax[0].set_xlabel("time(s)")
ax[0].set_ylabel("amplitube")
ax[0].plot(time_line, signal)

# plot spectrum
ax[1].grid()
ax[1].set_xlim(left=0, right=max(freqs))
ax[1].set_ylim(bottom=0, top=1.05)
ax[1].set_xlabel("Hz")
ax[1].set_ylabel("normalized amplitube")
ax[1].plot(freqs, normalized_spectrum[0:max_point])