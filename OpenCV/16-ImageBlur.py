import cv2

img = cv2.imread('./res/mini.jpeg')
cv2.imshow('org', img)
kernelsizes = [(3,3), (9,9), (15, 15)]

for kernel in kernelsizes:
    blur = cv2.blur(img, kernel)
    cv2.imshow('Average : ' + str(kernel), blur)

for kernel in kernelsizes:
    gaussian = cv2.GaussianBlur(img, kernel, 0)
    cv2.imshow('Gaussian : ' + str(kernel), gaussian)

for kernel in (3, 9, 15):
    median = cv2.medianBlur(img, kernel)
    cv2.imshow('MedianBlur : ' + str(kernel), median)

params = [(90, 50, 10), (50, 90, 10), (10, 90, 50)]
for p1, p2, p3 in params:
    bilateral = cv2.bilateralFilter(img, p1, p2, p3)
    cv2.imshow('bilateral' + str((p1, p2, p3)), bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()