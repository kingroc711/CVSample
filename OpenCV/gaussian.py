import cv2
import numpy as np

img = cv2.imread('./res/board.jpg')
cv2.imshow('lenna', img)

g_img = cv2.GaussianBlur(img,(7,7),5)
cv2.imshow('gaussian_blur_lenna7x7', g_img)

g_img = cv2.GaussianBlur(img,(17,17),5)
cv2.imshow('gaussian_blur_lenna17x17', g_img)

g_img = cv2.GaussianBlur(img,(7,7),1)
cv2.imshow('gaussian_blur_lenna simg1', g_img)

key = cv2.waitKey()
cv2.destroyAllWindows()