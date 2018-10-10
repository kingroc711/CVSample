import cv2

cameraCapture = cv2.VideoCapture('./res/test.mp4')
print(cameraCapture.get(cv2.CAP_PROP_POS_MSEC))
print(cameraCapture.get(cv2.CAP_PROP_POS_FRAMES))
print(cameraCapture.get(cv2.CAP_PROP_POS_AVI_RATIO))
print(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT))
