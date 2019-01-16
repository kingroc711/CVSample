import cv2 as cv
from cv2 import dnn

cap = cv.VideoCapture('./res/test.mp4')
net = dnn.readNetFromCaffe('./res/deploy.prototxt', './res/res10_300x300_ssd_iter_140000.caffemodel')

inWidth = 300
inHeight = 300
confThreshold = 0.5

while True:
    ret, frame = cap.read()
    cols = frame.shape[1]
    rows = frame.shape[0]

    net.setInput(dnn.blobFromImage(frame, 1.0, (inWidth, inHeight), (104.0, 177.0, 123.0), False, False))
    detections = net.forward()
    # perf_stats = net.getPerfProfile()
    # print('Inference time, ms: %.2f' % (perf_stats[0] / cv.getTickFrequency() * 1000))
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > confThreshold:
            xLeftBottom = int(detections[0, 0, i, 3] * cols)
            yLeftBottom = int(detections[0, 0, i, 4] * rows)
            xRightTop = int(detections[0, 0, i, 5] * cols)
            yRightTop = int(detections[0, 0, i, 6] * rows)

            cv.rectangle(frame, (xLeftBottom, yLeftBottom), (xRightTop, yRightTop), (0, 0, 255))
            if cv.waitKey(30) == 27:
                break;

    cv.imshow("detections", frame)
    if cv.waitKey(1) == 27:
        break

cv.destroyAllWindows()

