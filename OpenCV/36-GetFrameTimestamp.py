import cv2

cameraCapture = cv2.VideoCapture('./res/2_003_013.mp4')

success, frame = cameraCapture.read()
while success:
    if cv2.waitKey(1) == 27:
        break
    cv2.imshow('Test camera', frame)
    success, frame = cameraCapture.read()
    msec = cameraCapture.get(cv2.CAP_PROP_POS_MSEC)
    print(msec)

cv2.destroyAllWindows()
cameraCapture.release()