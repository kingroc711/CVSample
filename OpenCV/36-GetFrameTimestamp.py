import cv2

cameraCapture = cv2.VideoCapture('./res/2_003_013.mp4')

success, frame = cameraCapture.read()
while success:
    if cv2.waitKey(1) == 27:
        break
    cv2.imshow('Test camera', frame)
    success, frame = cameraCapture.read()
    milliseconds = cameraCapture.get(cv2.CAP_PROP_POS_MSEC)

    seconds = milliseconds//1000
    milliseconds = milliseconds%1000
    minutes = 0
    hours = 0
    if seconds >= 60:
        minutes = seconds//60
        seconds = seconds % 60

    if minutes >= 60:
        hours = minutes//60
        minutes = minutes % 60

    print(int(hours), int(minutes), int(seconds), int(milliseconds))

cv2.destroyAllWindows()
cameraCapture.release()