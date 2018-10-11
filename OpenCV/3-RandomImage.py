import cv2
import numpy
import os

randomByteArray = bytearray(os.urandom(300*400))
flatNumpyArray = numpy.array(randomByteArray)

grayImage = flatNumpyArray.reshape(300, 400)
cv2.imwrite('./out/RandomGray.png', grayImage)

bgrImage = flatNumpyArray.reshape(100, 400, 3)
cv2.imwrite('./out/RandomColor.png', bgrImage)
