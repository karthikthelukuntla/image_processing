import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

def affine_traformation_rotation(img, rotationAngle):

    center = tuple(np.array(img.shape[0:2]) / 2)
    rot_mat = cv2.getRotationMatrix2D(center, rotationAngle, 1.0)
    return cv2.warpAffine(img, rot_mat, img.shape[0:2], flags=cv2.INTER_NEAREST)

# Used basic formula to rotate an image. Affine trasformation uses advanced way to get
# quality output.
def rotate_image_without_interpolation(img, rotationAngle):

    # Source image dimensions
    h = img.shape[0]
    w = img.shape[1]

    # Finding center of the source image
    xm, ym = tuple(np.array(img.shape[0:2]) / 2)

    # Declaring empty numpy array to store output pixcels
    rotate_img = np.zeros((w, h))

    for i in range(0, h):
        for j in range(0, w):
            try:
                new_x_position = math.floor((i - xm) * math.cos(rotationAngle) - (j-ym) * math.sin(rotationAngle) + xm)
                new_y_position = math.floor((i - xm) * math.sin(rotationAngle) + (j-ym) * math.cos(rotationAngle) + ym)

                rotate_img[new_x_position, new_y_position] = img[i, j]

            except IndexError:
                pass

    return rotate_img

def image_show(img):
    cv2.imshow("OrgImg", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Reading image
img = cv2.imread("../pic.jpg", cv2.IMREAD_GRAYSCALE)

# Rotating image without interpolation
img_without_interpolation = rotate_image_without_interpolation(img, math.pi/4)

# Rotating image using affine transformation
img_with_interpolation = affine_traformation_rotation(img, 45)

fig = plt.figure(figsize=(12, 10))
ax1 = fig.add_subplot(2, 2, 1)
ax1.title.set_text("Actual Image")
ax1.imshow(img, cmap='gray')

ax2 = fig.add_subplot(2, 2, 2)
ax2.title.set_text("Rotated Image with Affine Transformation(with interpolation)")
ax2.imshow(img_with_interpolation, cmap='gray')

ax3 = fig.add_subplot(2, 2, 3)
ax3.title.set_text("Rotated Image without Interpolation")
ax3.imshow(img_without_interpolation, cmap='gray')

ax4 = fig.add_subplot(2, 2, 4)
ax4.title.set_text("Rotated Image with Interpolation")
# Apply interpolation while displaying image
ax4.imshow(img_without_interpolation, cmap='gray', interpolation='bicubic')

plt.show(block=True)

