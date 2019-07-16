import cv2
import numpy as np


img = cv2.imread('./res/board.jpg')
cv2.imshow('lenna', img)

print(img.shape)

img_gray = np.float32(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))

img_harris = cv2.cornerHarris(img_gray, 2, 3, 0.05)
cv2.imshow('img_harris ', img_harris)

thres = 0.05 * np.max(img_harris)
img[img_harris > thres] = [0, 0, 255]
cv2.imshow('img_harris 2', img)

sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(img,None)
kp,des = sift.compute(img,kp)
img_sift= cv2.drawKeypoints(img,kp,outImage=np.array([]), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('lenna_sift.jpg', img_sift)



key = cv2.waitKey()
cv2.destroyAllWindows()

