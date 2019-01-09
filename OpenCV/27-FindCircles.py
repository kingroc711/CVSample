import cv2 as cv
import numpy as np


src = cv.imread('./res/board.jpg', cv.IMREAD_COLOR)
img = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
img = cv.medianBlur(img, 5)
cimg = src.copy()

circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 10, np.array([]), 100, 30, 1, 20)
if circles is not None:
    a, b, c = circles.shape
    print(str(circles))
    for i in range(b):
        cv.circle(cimg, (circles[0][i][0], circles[0][i][1]), circles[0][i][2], (0, 0, 255), 3, cv.LINE_AA)
        cv.circle(cimg, (circles[0][i][0], circles[0][i][1]), 2, (0, 255, 0), 3, cv.LINE_AA)  # draw center of circle

    cv.imshow("detected circles", cimg)

cv.waitKey(0)