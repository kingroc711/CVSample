import cv2

img = cv2.imread('./res/aero3.jpg')
print(img.shape[:2])

height, width = img.shape[:2]

M = cv2.getRotationMatrix2D((width/2, height/2), 90*2, 1)
img_ro = cv2.warpAffine(img, M, (width, height))

cv2.imshow('rotation', img_ro)

cv2.waitKey()
cv2.destroyAllWindows()
