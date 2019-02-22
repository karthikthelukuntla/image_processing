## image_processinig
  This repository contains basic image operations.
  ### How to Use:
  Just install dependency packages like openCV (cv2), numpy, matplotlib. I recomend to use PyCharm because it is easy to setup as it ask to install all required packages once we import the project.
  After seting up environment run each python file to see the outputs.
  ### Histogram equalization:
  If image contrast is low, that means Histogram of image is limited to some values. To increase the contrast we need to strech or spread the instogram to all the values.
  Histogram of a image is a plot between intensity values (0 to 255) on X-axis and number of pixcels taking each intensity value on Y-Axis. You can check out examples of different Histograms techniques in my examples.
  ### Interpolation:
  It is a method of constructing new data points within the range of a discrete set of known data points.
  When we do scaling or rotating an image, it will create new pixcels, to fill the intensity value in these pixcels, we use interpolation. Check out interpolation folder for exmaples.
