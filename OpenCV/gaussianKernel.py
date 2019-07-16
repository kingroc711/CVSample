import cv2
import numpy as np

kernel = cv2.getGaussianKernel(7, 5)
print(kernel)

img = cv2.imread('./res/board.jpg')
cv2.imshow('lenna', img)

g1_img = cv2.GaussianBlur(img,(7,7),5)
g2_img = cv2.sepFilter2D(img, -1, kernel, kernel)

#cv2.imshow('g1_blur_lenna', g1_img)
#cv2.imshow('g2_blur_lenna', g2_img)

kernel_lap = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], np.float32)
lap_img = cv2.filter2D(img, -1, kernel=kernel_lap)
cv2.imshow('lap_lenna filter2D with kernel 1', lap_img)

kernel_sharp = np.array([[0, 1, 0], [1, -3, 1], [0, 1, 0]], np.float32)
lap_img = cv2.filter2D(img, -1, kernel=kernel_sharp)
cv2.imshow('lap_lenna filter2D with kernel 2', lap_img)

kernel_sharp = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
lap_img = cv2.filter2D(img, -1, kernel=kernel_sharp)
cv2.imshow('lap_lenna filter2D with kernel 3', lap_img)

kernel_sharp = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]], np.float32)
lap_img = cv2.filter2D(img, -1, kernel=kernel_sharp)
cv2.imshow('lap_lenna filter2D with kernel 4', lap_img)

edgex = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], np.float32)
sharp_img = cv2.filter2D(img, -1, kernel=edgex)
cv2.imshow('lap_lenna filter2D with kernel 5', sharp_img)

edgey = np.array([[-1, 0, -1], [-2, 0, 2], [-1, 0, 1]], np.float32)
sharpy_img = cv2.filter2D(img, -1, kernel=edgey)
cv2.imshow('lap_lenna filter2D with kernel 6', sharpy_img)

key = cv2.waitKey()
cv2.destroyAllWindows()