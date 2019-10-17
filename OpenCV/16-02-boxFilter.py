import cv2

img = cv2.imread('./res/mini.jpeg')
cv2.imshow('org', img)
kernelsizes = [(3,3), (9,9), (15, 15)]

for kernel in kernelsizes:
    blur = cv2.boxFilter(img, -1, kernel, anchor=(-1,-1), normalize=True, borderType=cv2.BORDER_DEFAULT)
    cv2.imshow('Average : ' + str(kernel), blur)

cv2.waitKey(0)
cv2.destroyAllWindows()