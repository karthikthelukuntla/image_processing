import cv2
import numpy as np
import math
import matplotlib.pyplot as plt


def opencv_resize(img, scale_width, scale_height):

    height, width = img.shape[:2]
    return cv2.resize(img, (scale_width * width, scale_height * height), interpolation=cv2.INTER_CUBIC)

# I just used simple scaling of image by just multiplying each pixcel with scaling factor.
# OpenCV resize function uses advanced approach to get better results. You can see the difference in output.
def resize_without_interpolation(img, scale_width, scale_height):
    # Source image dimensions
    h = img.shape[0]
    w = img.shape[1]

    print(h,w)
    # Declaring empty numpy array
    scaled_img = np.zeros((scale_width * h, scale_height * w))

    for i in range(0, h):
        try:
            for j in range(0, w):
                    scaled_img[scale_width * i, scale_height * j] = img[i, j]
        except IndexError as e:
            print(e)
            print(scale_width * i, scale_height * j)
            break

    return scaled_img

# Reading image
img = cv2.imread("../pic.jpg", cv2.IMREAD_GRAYSCALE)

img_resize = opencv_resize(img, 2, 2)

img_without_interpolation = resize_without_interpolation(img, 2, 2)

fig = plt.figure(figsize=(12, 10))
ax1 = fig.add_subplot(2, 2, 1)
ax1.imshow(img, cmap='gray')
ax1.title.set_text("Actual Image")

ax2 = fig.add_subplot(2, 2, 2)
ax2.title.set_text("Scaled image using openCV resize (with interpolation)")
ax2.imshow(img_resize, cmap='gray')

ax3 = fig.add_subplot(2, 2, 3)
ax3.title.set_text("Scaled Image without Interpolation")
ax3.imshow(img_without_interpolation, cmap='gray')

ax4 = fig.add_subplot(2, 2, 4)
ax4.title.set_text("Scaled Image with Interpolation")
# Apply interpolation while displaying image
ax4.imshow(img_without_interpolation, cmap='gray', interpolation='bicubic')

plt.show(block=True)
