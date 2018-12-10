import cv2
import os

cameraCapture = cv2.VideoCapture('./res/test.mp4')

detector = cv2.CascadeClassifier(os.getcwd() + '/XML/haarcascade_frontalface_alt_tree.xml')

model_zxc = cv2.face.EigenFaceRecognizer_create()
model_zxc.read(os.getcwd() + '/XML/actor_zxc.xml')
print(os.getcwd() + '/XML/actor_cl.xml')

cv2.namedWindow('Test camera')
success, frame = cameraCapture.read()
while success:
    success, frame = cameraCapture.read()
    rects = detector.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=2, minSize=(100, 100),
                                      flags=cv2.CASCADE_SCALE_IMAGE)
    if len(rects) > 0:
        for (x, y, w, h) in rects:
            face = cv2.resize(frame[y:y+h, x:x+w], (200, 200))
            gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            params = model_zxc.predict(gray)
            print(params)
            if params[1] < 5500.0:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1)
            else:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
        if cv2.waitKey(1) == 27:
            break
        cv2.imshow('Test camera', frame)

cv2.destroyAllWindows()
cameraCapture.release()