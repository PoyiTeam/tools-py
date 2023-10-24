import cv2
import numpy as np


def cv2_readimg(file_path):
    # for cv2 reading chinese path
    # input : file path,
    # output : image array
    file_path = np.fromfile(file_path, dtype=np.uint8)
    image = cv2.imdecode(file_path, -1)

    return image
