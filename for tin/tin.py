# %%
import numpy as np
import cv2
import os

# %%

img = cv2.imread('IMG_5733_mod.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_source_size = np.array(img_gray.shape)
img_mod_size = np.around(img_source_size * 0.5).astype('int32')
# %%
img_mod = cv2.resize(img_gray, img_mod_size, interpolation=cv2.INTER_AREA)
np.save('img_mod.npy', img_mod)
