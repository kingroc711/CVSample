import cv2
import numpy as np

image = cv2.imread('./res/aero3.jpg')
M = np.float32([[1, 0, 10], [0, 1, 50]])
moveImage = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow('move', moveImage)
cv2.waitKey()
cv2.destroyAllWindows()