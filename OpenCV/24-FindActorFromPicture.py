import cv2
import os

img = cv2.imread('./res/zrfGrouphoto.jpeg')

path = os.getcwd() + '/XML/haarcascade_frontalface_alt2.xml'
detector = cv2.CascadeClassifier(path)
rects = detector.detectMultiScale(img, scaleFactor=1.1, minNeighbors=2, minSize=(10, 10), flags=cv2.CASCADE_SCALE_IMAGE)


model_zrf = cv2.face.EigenFaceRecognizer_create()
model_zrf.read(os.getcwd() + '/XML/actor_zrf.xml')
for(x, y, w, h) in rects:
    face = cv2.resize(img[y:y + h, x:x + w], (200, 200))
    gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    params = model_zrf.predict(gray)
    print(params[1])
    if params[1] < 8100.0:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 1)
    # else:
    #     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
cv2.imshow('face', img)
cv2.waitKey(0)
cv2.destroyAllWindows()