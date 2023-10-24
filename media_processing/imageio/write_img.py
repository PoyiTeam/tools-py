# %%
import imageio.v3 as imgio
import numpy as np

# %%

img_name1 = "test_img1.png"
img_name2 = "test_img2.png"

# create an example image
#img = imgio.imread('imageio:astronaut.png')
img = np.random.rand(300, 300)
img1 = np.round(img*256).astype("uint8")
img2 = np.round(img*65536).astype("uint16")
print(img1)
print(img2)

# png-encoded bytes string
png_encoded = imgio.imwrite(img_name1, img1, format_hint=".png")
png_encoded = imgio.imwrite(img_name2, img2, format_hint=".png")
#png_encoded = imgio.imwrite(img_name, img, format_hint=".png")

# jpg-encoded bytes string
jpg_encoded = imgio.imwrite("<bytes>", img, format_hint=".jpeg")

# RGBA bytes string
img = imgio.imread('imageio:astronaut.png', mode="RGBA")
png_encoded = imgio.imwrite("<bytes>", img, format_hint=".png")
