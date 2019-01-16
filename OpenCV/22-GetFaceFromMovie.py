import cv2
import os

cameraCapture = cv2.VideoCapture('./res/test.mp4')

path = os.getcwd() + '/XML/haarcascade_frontalface_alt_tree.xml'
detector = cv2.CascadeClassifier(path)

cv2.namedWindow('Test camera')
success, frame = cameraCapture.read()
while success:
    if cv2.waitKey(1) == 27:
        break
    success, frame = cameraCapture.read()
    rects = detector.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=2, minSize=(100, 100),
                                      flags=cv2.CASCADE_SCALE_IMAGE)
    if len(rects) > 0:
        for (x, y, w, h) in rects:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1)
    cv2.imshow('Test camera', frame)

cv2.destroyAllWindows()
cameraCapture.release()