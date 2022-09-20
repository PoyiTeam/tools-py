import numpy as np


"""
v20220705
"""


def get_frame_idx(data, window_size, stride):
    """
    function for splitting data / making frames

    data : array-like
        1d numerical array data
    window size : int
        frame size
    stride : int
        shift points of each step

    return
        frame_idx : ndarray
            array of frames index
    """
    data_len = len(data)
    remainder = data_len % stride
    end_point = data_len - remainder

    start_point = 0
    idx_range = np.zeros((1, 2), dtype="int32")
    frame_idx = np.array([[start_point, window_size]])
    start_point += stride

    while start_point + window_size <= end_point:
        idx_range[0, 0] = start_point
        idx_range[0, 1] = start_point + window_size
        frame_idx = np.concatenate((frame_idx, idx_range))
        start_point += stride

    return frame_idx
