import cv2
import numpy as np

img = cv2.imread('./res/aero3.jpg')
print(img.shape[:2])

width, height = img.shape[:2]

M = cv2.getRotationMatrix2D((width/2, height/2), 45, 1)
img_ro = cv2.warpAffine(img, M, img.shape[:2])
cv2.imshow('rotation', img_ro)

cv2.waitKey()
cv2.destroyAllWindows()