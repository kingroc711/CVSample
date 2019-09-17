import cv2 as cv
import numpy as np

def func2(img):
    (B, G, R) = cv.split(img)

    #创建2个空白图层
    new1 = np.zeros(img.shape[0:2], img.dtype)
    new2 = np.zeros(img.shape[0:2], img.dtype)

    #提取红色、蓝色数值明显大于蓝色的像素。
    new1[R/1.5 > B] = 1
    new2[G/1.5 > B] = 1
    new1 = new1 & new2

    #获取红色和绿色数值相同的像素点。
    new2[G - R == 0] = 1

    #继续获取焦急。
    new1 = new1 & new2
    #将黄色点置为最亮。
    new1[new1 == 1] = 255
    return new1

img = cv.imread('./res/IMG00868.jpg', cv.IMREAD_COLOR)
height, width = img.shape[:2]
print("height : " + str(height) + ', width : ' + str(width))

cv.namedWindow('org', 0)
cv.imshow('org', img)
new1 = func2(img)

cv.namedWindow('new', 0)
cv.imshow('new', new1)

cv.namedWindow('blur', 0)
blur = cv.medianBlur(new1, 17)
cv.imshow('blur', blur)

while(1):
    if(cv.waitKey(100)==27):
        break
