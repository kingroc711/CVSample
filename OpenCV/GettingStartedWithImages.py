import numpy as np
import cv2 as cv
import sys
import platform
from distutils.sysconfig import get_python_lib;
from distutils.sysconfig import get_python_version;

print(get_python_version())
print(get_python_lib())

#print(sys.version)
print(np.get_include())

img = cv.imread('./res/aero3.jpg', 0)
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyWindow()


