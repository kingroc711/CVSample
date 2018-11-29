import cv2

img = cv2.imread('./res/mini.jpeg')
imgH = cv2.flip(img, 1)
imgV = cv2.flip(img, 0)
imgHV = cv2.flip(img, -1)

cv2.imshow('img', img)
cv2.imshow('imgH', imgH)
cv2.imshow('imgV', imgV)
cv2.imshow('imgHV', imgHV)
cv2.waitKey()
cv2.destroyAllWindows()