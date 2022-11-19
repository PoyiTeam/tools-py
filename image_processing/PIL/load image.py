#%% direct open image
# load and show an image with Pillow
import PIL

# Open the image form working directory
image = PIL.Image.open("example image.jpg")
# summarize some details about the image
print(image.format)
print(image.size)
print(image.mode)
# show the image
image.show()

#%% direct
# load and display an image with Matplotlib
from matplotlib import image
import matplotlib.pyplot as plt

# load image as pixel array
image = image.imread("example image.jpg")
# summarize shape of the pixel array
print(image.dtype)
print(image.shape)
# display the array of pixels as an image
plt.imshow(image)
plt.show()

#%% image as array
import numpy as np

# load the image
image = PIL.Image.open("example image.jpg")
# convert image to numpy array
data = np.asarray(image)
print(type(data))
# summarize shape
print(data.shape)

# create Pillow image
image2 = PIL.Image.fromarray(data)
print(type(image2))

# summarize image details
print(image2.mode)
print(image2.size)
