import cv2 as cv
import numpy as np


src = cv.imread('./res/IMG00868.jpg', cv.IMREAD_COLOR)
height, width = src.shape[:2]
print("height : " + str(height) + ', width : ' + str(width))

img = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
img = cv.medianBlur(img, 5)
cimg = src.copy()

circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 900, np.array([]), 100, 30, 500, 1000)
if circles is not None:
    a, b, c = circles.shape
    print(str(circles))
    for i in range(b):
        if(circles[0][i][0] + circles[0][i][2] < width and circles[0][i][1] + circles[0][i][2] < height and circles[0][i][2] < circles[0][i][0] and circles[0][i][2] < circles[0][i][1]):
            cv.circle(cimg, (circles[0][i][0], circles[0][i][1]), circles[0][i][2], (0, 0, 255), 3, cv.LINE_AA)
            cv.circle(cimg, (circles[0][i][0], circles[0][i][1]), 2, (0, 255, 0), 3, cv.LINE_AA)  # draw center of circle
            print(circles[0][i][0])
            print(circles[0][i][1])
            print(circles[0][i][2])

    #cv.imshow("detected circles", cimg)
    cv.imwrite('./res/IMG00868C.jpg', cimg)

cv.waitKey(0)