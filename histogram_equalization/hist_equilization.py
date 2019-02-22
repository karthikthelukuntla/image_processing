import cv2
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(12, 10))

# Reading image
img = cv2.imread("pic.jpg", cv2.IMREAD_GRAYSCALE)

ax1 = fig.add_subplot(3, 2, 1)
ax1.title.set_text("Original Image")
ax1.imshow(img, cmap='gray')

ax2 = fig.add_subplot(3, 2, 2)
ax2.title.set_text("Original Image Histogram")
ax2.hist(img.flatten(), 256, [0, 256], color='r')

# Histgram equalised image
equilized_image = cv2.equalizeHist(img)

ax2 = fig.add_subplot(3, 2, 3)
ax2.title.set_text("Histogram equalized Image")
ax2.imshow(equilized_image, cmap='gray')

ax2 = fig.add_subplot(3, 2, 4)
ax2.title.set_text("equalized Image Histogram")
ax2.hist(equilized_image.flatten(), 256, [0, 256], color='r')

# CLAHE (Contrast Limited Adaptive Histogram Equalization)
# Image is divided into small blocks called "tiles". Then each of these blocks are histogram equalized as usual

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
adaptive_hist_eq = clahe.apply(img)

ax2 = fig.add_subplot(3, 2, 5)
ax2.title.set_text("Adaptive Histogram Equalized Image")
ax2.imshow(adaptive_hist_eq, cmap='gray')

ax2 = fig.add_subplot(3, 2, 6)
ax2.title.set_text("Adaptive equalized Image Histogram")
ax2.hist(adaptive_hist_eq.flatten(), 256, [0, 256], color='r')

plt.show(block=True)
