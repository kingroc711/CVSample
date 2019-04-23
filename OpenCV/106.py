import cv2
import numpy as np

videoLeftUp = cv2.VideoCapture('./res/2_003_013.mp4')
videoLeftDown = cv2.VideoCapture('./res/2_003_014.mp4')
videoRightUp = cv2.VideoCapture('./res/2_003_015.mp4')
videoRightDown = cv2.VideoCapture('./res/2_003_016.mp4')

fps = videoLeftUp.get(cv2.CAP_PROP_FPS)

width = (int(videoLeftUp.get(cv2.CAP_PROP_FRAME_WIDTH)))
height = (int(videoLeftUp.get(cv2.CAP_PROP_FRAME_HEIGHT)))

#videoWriter = cv2.VideoWriter('./out/4in1.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, (width, height))

successLeftUp, frameLeftUp = videoLeftUp.read()
successLeftDown , frameLeftDown = videoLeftDown.read()
successRightUp, frameRightUp = videoRightUp.read()
successRightDown, frameRightDown = videoRightDown.read()

while successLeftUp and successLeftDown and successRightUp and successRightDown:
    frameLeftUp = cv2.resize(frameLeftUp, (int(width / 2), int(height / 2)), interpolation=cv2.INTER_CUBIC)
    frameLeftDown = cv2.resize(frameLeftDown, (int(width / 2), int(height / 2)), interpolation=cv2.INTER_CUBIC)
    frameRightUp = cv2.resize(frameRightUp, (int(width / 2), int(height / 2)), interpolation=cv2.INTER_CUBIC)
    frameRightDown = cv2.resize(frameRightDown, (int(width / 2), int(height / 2)), interpolation=cv2.INTER_CUBIC)

    frameUp = np.hstack((frameLeftUp, frameRightUp))
    frameDown = np.hstack((frameLeftDown, frameRightDown))
    frame = np.vstack((frameUp, frameDown))


    if cv2.waitKey(1) == 27:
        break
    cv2.imshow('Test camera', frame)
    successLeftUp, frameLeftUp = videoLeftUp.read()
    successLeftDown, frameLeftDown = videoLeftDown.read()
    successRightUp, frameRightUp = videoRightUp.read()
    successRightDown, frameRightDown = videoRightDown.read()

#videoWriter.release()
videoLeftUp.release()
videoLeftDown.release()
videoRightUp.release()
videoRightDown.release()