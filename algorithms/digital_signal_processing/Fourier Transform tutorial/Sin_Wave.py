#%%
import numpy as np  # 矩陣運算啦
import matplotlib.pyplot as plt  # 畫圖啦
from scipy.fft import fft  # fast Fourier transform

#%% 創造時間軸
start_time = 0  # 起始時間
end_time = 1  # 結束時間
sampling_rate = 8000  # 採樣頻率
time_step = 1 / sampling_rate  # 每一格點的時間間隔
point_num = int((end_time - start_time) * sampling_rate)  # x軸點位數量

time = np.linspace(start=start_time, stop=end_time, num=point_num)

#%% 創建sin wave
amp_1 = 0.5
sin1_freq = 5  # 設定sin wave頻率
sin1 = amp_1 * np.sin(2 * np.pi * sin1_freq * time)  # sin wave 1

amp_2 = 1
sin2_freq = 7
sin2 = amp_2 * np.sin(2 * np.pi * sin2_freq * time)  # sin wave 2

amp_3 = 1.5
sin3_freq = 200
sin3 = amp_3 * np.sin(2 * np.pi * sin3_freq * time)  # sin wave 2

amp_4 = 0.2
sin4_freq = 400
sin4 = amp_4 * np.sin(2 * np.pi * sin4_freq * time)  # sin wave 2

amp_5 = 0.1
sin5_freq = 800
sin5 = amp_5 * np.sin(2 * np.pi * sin5_freq * time)  # sin wave 2

x = time
y = sin1 + sin2  # 最後輸出的訊號

plt.figure(figsize=(20, 5))  # 設定圖形大小
plt.xlim([start_time, end_time])  # 設定圖形 x軸 範圍
plt.ylim([-3, 3])  # 設定圖形 y軸 範圍
plt.xlabel("time (s)")
plt.ylabel("amplitude")
plt.plot(x, y)  # 畫圖囉

#%% Fourier tranform
signal = y

signal_fft = fft(signal)  # 快速傅立葉轉換
spectrum = abs(signal_fft)  # 取得頻譜圖
max_freq = sampling_rate / 2  # 最大有效頻率為採樣頻率的一半

x_freq = np.linspace(start=0, stop=max_freq, num=int(len(signal) / 2))  #頻率
y_spectrum = spectrum[0:int(len(signal) / 2)]

plt.figure(figsize=(20, 5))
plt.plot(x_freq, y_spectrum)
plt.xlabel("frequency")
plt.ylabel("power")
plt.xlim([0, sampling_rate / 2])
plt.ylim([0, max(y_spectrum)])
# %%
