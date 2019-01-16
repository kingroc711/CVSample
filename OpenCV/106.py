import cv2 as cv
from cv2 import dnn


img = cv.imread('/home/king/Desktop/1.png')
net = dnn.readNetFromCaffe('./res/deploy.prototxt', './res/res10_300x300_ssd_iter_140000.caffemodel')

net.setInput(dnn.blobFromImage(img, 1.0, (300, 300), (104.0, 177.0, 123.0), False, False))
detections = net.forward()

cols = img.shape[1]
rows = img.shape[0]

for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    if confidence > 0.5:
        xLeftBottom = int(detections[0, 0, i, 3] * cols)
        yLeftBottom = int(detections[0, 0, i, 4] * rows)
        xRightTop = int(detections[0, 0, i, 5] * cols)
        yRightTop = int(detections[0, 0, i, 6] * rows)

        cv.rectangle(img, (xLeftBottom, yLeftBottom), (xRightTop, yRightTop), (0, 0, 255))
cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()