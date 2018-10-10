import cv2

clicked = False

def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True


cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('MyWindow')
cv2.setMouseCallback('MyWindow', onMouse)

success, frame = cameraCapture.read()
while success:
    keycode = cv2.waitKey(1)
    if(keycode == 27):
        break
    cv2.imshow('MyWindow',frame)
    success, frame = cameraCapture.read()

cameraCapture.release()


# import cv2
# import numpy as np
#
# cap = cv2.VideoCapture(0)
# while(1):
#     # get a frame
#     ret, frame = cap.read()
#     # show a frame
#     cv2.imshow("capture", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()