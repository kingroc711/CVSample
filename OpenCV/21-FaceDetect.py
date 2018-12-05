import cv2
import os

img = cv2.imread('./res/face.jpeg')

path = os.getcwd() + '/XML/haarcascade_frontalface_alt2.xml'
detector = cv2.CascadeClassifier(path)
rects = detector.detectMultiScale(img, scaleFactor=1.1, minNeighbors=2, minSize=(10, 10), flags=cv2.CASCADE_SCALE_IMAGE)
for(x, y, w, h) in rects:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 1)

path = os.getcwd() + '/XML/haarcascade_eye_tree_eyeglasses.xml'
detector = cv2.CascadeClassifier(path)
rects = detector.detectMultiScale(img, scaleFactor=1.1, minNeighbors=2, minSize=(10, 10), flags=cv2.CASCADE_SCALE_IMAGE)
for(x, y, w, h) in rects:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 1)

cv2.imshow('face', img)
cv2.waitKey(0)
cv2.destroyAllWindows()