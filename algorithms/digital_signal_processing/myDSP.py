"""
v20220908

module for digital signal process
"""

import numpy as np
from scipy import signal


def enframe(data, window_len: int, stride: int, cut_tail=True):
    """
    function for splitting data / making window

    data : array-like
        numerical array data
    window size : int
        window size
    stride : int
        shift points of each step

    return
        window_idx : ndarray
            array of windows index
    """
    data_len = len(data)
    remainder = data_len % stride
    end_point = data_len - remainder

    start_point = 0
    idx_range = np.zeros((1, 2), dtype=np.int32)
    window_idx = np.array([[start_point, window_len]])
    start_point += stride

    while start_point + window_len <= end_point:
        idx_range[0, 0] = start_point
        idx_range[0, 1] = start_point + window_len
        window_idx = np.concatenate((window_idx, idx_range))
        start_point += stride

    if cut_tail:
        return window_idx
    else:
        idx_last = np.array([[idx_range[0, 1], data_len]])
        window_idx = np.hstack((window_idx, idx_last))
        return window_idx


def power_spectrum(data):
    return np.abs(np.fft.rfft(data))


def amplitude_envelope(data):
    return np.abs(signal.hilbert(data))


def freq_axis(window_len: int, fs):
    """
    get 1D array refer to window length and sampling rate
    """
    return np.fft.rfftfreq(window_len, 1 / fs)


def focus_spectrum_band(freqs, band_range):
    """
    freqs: array-like
        frequency axis refer to spectrum
    band_range: array-like, length=2
        band_range[0] = start frequency
        band_range[1] = end frequency
    """
    if band_range[0] < 0:
        raise ValueError('band start frequency must greater than 0')
    if band_range[1] > freqs[-1]:
        band_range[1] = freqs[-1]

    start_idx = np.squeeze(np.where(freqs >= band_range[0])[0])[0]
    end_idx = np.squeeze(np.where(freqs >= band_range[1])[0])[0]+1

    band_range_idx = np.array([start_idx, end_idx])
    band_freqs = freqs[start_idx:end_idx]
    return band_freqs, band_range_idx


def get_spectrum_len(window_len: int) -> int:
    """
    return spectrum length refer to window length
    """
    if window_len % 2 == 0:
        spectrum_len = int(window_len * 0.5) + 1
    elif window_len % 2 == 1:
        spectrum_len = int(np.ceil(window_len * 0.5))
    else:
        print('something went wrong while ')
    return spectrum_len


def batch_fft(chunks):
    """
    `chunks` : 2D-array-like
        contain windowed signal in each chunk, foramt: `[window_num, windowed_signal]`

    `return` :
        spectra
    """
    spectrum_len = get_spectrum_len(chunks.shape[1])
    spectra = np.zeros((chunks.shape[0], spectrum_len))
    for i, chunk in enumerate(chunks):
        spec = np.abs(np.fft.rfft(chunk))
        spectra[i] = spec

    return spectra


def lowpass(sig, cutoff, fs, order):

    sos = signal.butter(order, cutoff, 'lp', fs=fs, output='sos')
    sig_filtered = signal.sosfilt(sos, sig)
    return sig_filtered


def add_white_noise(sig, snr_db=20):

    sig_avg = np.mean(sig)
    sig_avg_db = 10 * np.log10(sig_avg)
    noise_avg_db = sig_avg_db - snr_db
    noise_avg_sig = 10**(noise_avg_db * 0.1)
    mean_noise = 0
    np.random.seed(0)
    noise_sig = np.random.normal(
        mean_noise, np.sqrt(noise_avg_sig), len(sig))
    noise_sig += sig    # output raw signal + white noise
    return noise_sig
