import cv2
import os

cameraCapture = cv2.VideoCapture('./res/test.mp4')

detector = cv2.CascadeClassifier(os.getcwd() + '/XML/haarcascade_frontalface_alt_tree.xml')

model_cl = cv2.face.EigenFaceRecognizer_create()
model_cl.read(os.getcwd() + '/XML/actor_cl.xml')
print(os.getcwd() + '/XML/actor_cl.xml')

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
            face = cv2.resize(frame[y:y+h, x:x+w], (200, 200))
            params = model_cl.predict(face)
            print(params)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 1)
    cv2.imshow('Test camera', frame)

cv2.destroyAllWindows()
cameraCapture.release()