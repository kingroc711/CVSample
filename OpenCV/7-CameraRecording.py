import cv2

cameraCapture = cv2.VideoCapture(0)

fps = cameraCapture.get(cv2.CAP_PROP_FPS)

size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

videoWriter = cv2.VideoWriter('./out/record.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'),
                              fps, size)
success, frame = cameraCapture.read()
numFrame = 5 * fps -1

while success and numFrame > 0:
        videoWriter.write(frame)
        success, frame = cameraCapture.read()
        numFrame -= 1

cameraCapture.release()
