import cv2 as cv
import numpy as np

img = cv.imread('./res/pic1.png', cv.IMREAD_COLOR)
img2 = img.copy()
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 200)
minLineLength = 50
maxLineGap = 10

lines = cv.HoughLinesP(edges, 1, np.pi/180, 40, np.array([]), minLineLength, maxLineGap)
a, b, c = lines.shape
for i in range(a):
    cv.line(img, (lines[i][0][0], lines[i][0][1]),
            (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 3, cv.LINE_AA )

cv.imshow('source', img2)
cv.imshow('lines', img)
cv.waitKey(0)
cv.destroyAllWindows()