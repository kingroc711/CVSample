import cv2 as cv

img = cv.imread('./res/freckle.jpeg')
cv.imshow('org', img)

for i in range(1, 6):
    sigmaColor = i * 10
    sigmaSpace = sigmaColor*2
    imgb = cv.bilateralFilter(img, 100, sigmaColor, sigmaSpace)
    cv.imshow('bilateral' + str(sigmaColor) + '-' + str(sigmaSpace), imgb)

cv.waitKey(0)
cv.destroyAllWindows()