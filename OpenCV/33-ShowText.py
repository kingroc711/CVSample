import cv2

img = cv2.imread('./res/aero3.jpg')

#           照片   /添加的文字    /左下角坐标  /字体                            /字体大小 /颜色            /字体粗细
cv2.putText(img, 'Hello World', (0,40),     cv2.FONT_HERSHEY_COMPLEX,       1,       (0, 255, 0),     1)
cv2.putText(img, 'Hello World', (0,80),     cv2.FONT_HERSHEY_PLAIN,         1,       (0, 0, 255),     1)
cv2.putText(img, 'Hello World', (0,120),    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,       (255, 0, 0),     2)
cv2.putText(img, 'Hello World', (0,160),    cv2.FONT_HERSHEY_DUPLEX,        1,       (255, 255, 255), 1)
cv2.putText(img, 'Hello World', (0,200),    cv2.FONT_HERSHEY_SIMPLEX,       1,       (0, 0, 0),       1)
cv2.putText(img, 'Hello World', (0,240),    cv2.FONT_HERSHEY_TRIPLEX,       1,       (150, 0, 180),   1)

cv2.imshow('imgHV', img)
cv2.waitKey()
cv2.destroyAllWindows()