import cv2

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
img = cv2.imread('./res/jeep.jpeg')
cv2.imshow('org', img)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=2)
cv2.imshow('open', opening)

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=2)
cv2.imshow('close', closing)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('gradient', gradient)

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow('tophat', tophat)

blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow('blackhat', blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()