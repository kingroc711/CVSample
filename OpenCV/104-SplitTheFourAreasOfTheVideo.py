import cv2
import numpy as np

cameraCapture = cv2.VideoCapture('./res/2_003_013.mp4')
width = int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cameraCapture.get(cv2.CAP_PROP_FPS)

videoWriterLeftUp = cv2.VideoWriter('./out/LeftUp.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, (width//2, height//2))
videoWriterLeftDown = cv2.VideoWriter('./out/LeftDown.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, (width//2, height//2))
videoWriterRightUp = cv2.VideoWriter('./out/RightUp.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, (width//2, height//2))
videoWriterRightDown = cv2.VideoWriter('./out/RightDown.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, (width//2, height//2))

success, frame = cameraCapture.read()
while success:
    frameLeftUp = frame[0:height//2, 0:width//2, :]
    videoWriterLeftUp.write(frameLeftUp)

    frameLeftDown = frame[height//2:height, 0:width//2, :]
    videoWriterLeftDown.write(frameLeftDown)

    frameRightUp = frame[0:height//2, width//2:width, :]
    videoWriterRightUp.write(frameRightUp)

    frameRightDown = frame[height//2:height, width//2:width, :]
    videoWriterRightDown.write(frameRightDown)

    success, frame = cameraCapture.read()

cameraCapture.release()
videoWriterLeftUp.release()
videoWriterLeftDown.release()
videoWriterRightUp.release()
videoWriterRightDown.release()
