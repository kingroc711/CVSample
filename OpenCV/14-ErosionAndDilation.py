import cv2

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
img = cv2.imread('./res/jeep.jpeg')
cv2.imshow('jeep', img)

erosion = cv2.erode(img, kernel, iterations=3)
cv2.imshow('erosion', erosion)

dilation = cv2.dilate(img, kernel, iterations=3)
cv2.imshow('dilation', dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()