import  cv2
import numpy as np

img = cv2.imread('./res/mini.jpeg')

(R, G, B) = cv2.split(img)

cv2.imshow('ORG', img)
cv2.imshow('R', R)
cv2.imshow('G', G)
cv2.imshow('B', B)

merged = cv2.merge([R, G, B])
cv2.imshow('Merged', merged)

################
onlyR = np.zeros(img.shape, img.dtype)
onlyR[:, :, 0] = img[:, :, 0]
cv2.imshow('onlyR', onlyR)

onlyG = np.zeros(img.shape, img.dtype)
onlyG[:, :, 1] = img[:,:,1]
cv2.imshow('onlyG', onlyG)

onlyB = np.zeros(img.shape, img.dtype)
onlyB[:, :, 2] = img[:, :, 2]
cv2.imshow('onlyB', onlyB)

ColorMer = np.zeros(img.shape, img.dtype)
ColorMer[:, :, 0] = onlyR[:, :, 0]
ColorMer[:, :, 1] = onlyG[:, :, 1]
ColorMer[:, :, 2] = onlyB[:, :, 2]
cv2.imshow('ColorMer', ColorMer)

cv2.waitKey()
cv2.destroyAllWindows()