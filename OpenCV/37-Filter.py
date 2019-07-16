import cv2
import numpy as np
hubble = cv2.imread("res/habo.jpeg", 0)
filter_small = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
hubble_small = cv2.filter2D(hubble, -1, filter_small)

filter_big = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
hubble_big = cv2.filter2D(hubble, -1, filter_big)


#hubble_filter_th = np.where(hubble_big < 80, 0, 1)
hubble_filter_th = np.where(hubble_small < 0, 0, np.where(hubble_small > 255, 255, hubble_small))
hubble_clip = hubble * hubble_filter_th

cv2.imshow("hubble", hubble)
cv2.imshow("small filter", hubble_small)
cv2.imshow("big filter", hubble_big)
cv2.imshow("hubble_filter", hubble_filter_th.astype("uint8"))
cv2.imshow("hubble_clip", hubble_clip.astype("uint8"))



cv2.waitKey()
cv2.destroyAllWindows()