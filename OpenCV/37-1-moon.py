import cv2
import numpy as np

moon = cv2.imread("res/habo.jpeg", 0)
row, column = moon.shape
moon_f = np.copy(moon)
moon_f = moon_f.astype("float")

two = np.zeros((row, column))

for x in range(1, row - 1):
    for y in range(1, column - 1):
        two[x, y] = moon_f[x + 1, y] \
                    + moon_f[x - 1, y] \
                    + moon_f[x, y + 1] \
                    + moon_f[x, y - 1] \
                    - 4 * moon_f[x, y]

cv2.imshow("tow", two)
sharp = moon_f - two
sharp = np.where(sharp < 0, 0, np.where(sharp > 255, 255, sharp))
sharp = sharp.astype("uint8")

cv2.imshow("moon", moon)
cv2.imshow("sharp", sharp)
cv2.waitKey()
cv2.destroyAllWindows()