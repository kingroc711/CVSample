import  cv2
import numpy as np

img = cv2.imread('./res/aero3.jpg')
imgDown1 = cv2.pyrDown(img)
imgDown2 = cv2.pyrDown(imgDown1)
imgDown3 = cv2.pyrDown(imgDown2)

upImage1 = cv2.pyrUp(imgDown3)
upImage2 = cv2.pyrUp(upImage1)

lap = imgDown1 - upImage2
cv2.imshow('upImage', lap)

gray = cv2.cvtColor(lap, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()