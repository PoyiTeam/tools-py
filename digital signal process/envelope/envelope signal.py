#%%
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

#%%
signal = np.random.randint(low=-10, high=10, size=100)

#%%
signal_len = len(signal)
x = np.linspace(start=0, stop=signal_len, num=signal_len)

wave_peak_x = [0]
wave_peak_y = [signal[0]]
wave_trough_x = [0]
wave_trough_y = [signal[0]]

wave_max = 0
wave_min = 0

# detect peak and trough, then mark their location
for i in range(1, signal_len - 1):
    check_left = np.sign(signal[i] - signal[i - 1])
    check_right = np.sign(signal[i] - signal[i + 1])

    if check_left == 1 and check_right == 1:
        wave_peak_x.append(i)
        wave_peak_y.append(signal[i])

    elif check_left == -1 and check_right == -1:
        wave_trough_x.append(i)
        wave_trough_y.append(signal[i])

# append the last value of signal
wave_peak_x.append(signal_len - 1)
wave_peak_y.append(signal[-1])
wave_trough_x.append(signal_len - 1)
wave_trough_y.append(signal[-1])

# fit data with n-order curve.
upper_curve = interp1d(wave_peak_x,
                       wave_peak_y,
                       kind="cubic",
                       bounds_error=False,
                       fill_value=0.0)
lower_curve = interp1d(wave_trough_x,
                       wave_trough_y,
                       kind="cubic",
                       bounds_error=False,
                       fill_value=0.0)

envelope_curve_up = np.zeros(signal_len)
envelope_curve_low = np.zeros(signal_len)

for i in range(len(signal)):
    envelope_curve_up[i] = upper_curve(i)
    envelope_curve_low[i] = lower_curve(i)

envelope_curve_avg = (envelope_curve_up + envelope_curve_low) / 2
imf = signal - envelope_curve_avg  # intrinsic mode function

plt.plot(signal)
plt.plot(envelope_curve_up)
plt.plot(envelope_curve_low)
plt.plot(envelope_curve_avg)

plt.show()

plt.plot(imf)

# %%
