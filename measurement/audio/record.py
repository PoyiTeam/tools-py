#%%
import sounddevice as sd
import numpy as np

#%%
fs = 44100
duration = 3  # seconds
channel = 1

#%%
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channel)
sd.wait()
#%%
sd.play(myrecording, fs)
#%%
sd.query_devices()
