import numpy as np
import cv2
import matplotlib.pyplot as plt

def show(image):
    plt.imshow(image)
    plt.axis('off')
    plt.show()

image = np.zeros((400, 400,3), dtype='uint8')

red = (255, 0, 0)
cv2.line(image, (0,0), (400, 400), red)

green = (0, 255, 0)
cv2.line(image, (400, 0), (0,400), green, 5)

blue = (0, 0, 255)
cv2.rectangle(image, (200, 200), (250, 250), blue, 2)

white = (255, 255, 255)
cv2.rectangle(image, (20, 300), (40, 350), white, -1)

(cX, cY) = image.shape[1]//2, image.shape[0]//2

cv2.circle(image, (cX, cY - 100), 40, white, 2)

show(image)