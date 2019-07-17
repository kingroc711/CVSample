import cv2
import numpy as np


img = np.random.randint(1, 9, (5, 5))
print(img)

print('BORDER_CONSTANT\n', cv2.copyMakeBorder(img, 1,2,3,4, cv2.BORDER_CONSTANT, value=0))
print('BORDER_REPLICATE\n', cv2.copyMakeBorder(img, 1,2,3,4, cv2.BORDER_REPLICATE))
print('BORDER_REFLECT\n', cv2.copyMakeBorder(img, 1,2,3,4, cv2.BORDER_REFLECT))
print('BORDER_WRAP\n', cv2.copyMakeBorder(img, 1,2,3,4, cv2.BORDER_WRAP))