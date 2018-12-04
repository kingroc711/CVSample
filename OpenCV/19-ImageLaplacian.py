import cv2
from matplotlib import pyplot as plt

img = cv2.imread('./res/CarID.jpeg',0)
laplacian = cv2.Laplacian(img, cv2.CV_64F)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

sobleXplusY = sobelx + sobely

titles = ['Original', 'Laplacian', 'SobelX', 'SobelY', 'sobleXplusY']
imgs = [img, laplacian, sobelx, sobely, sobleXplusY]

plt.figure(figsize = (10, 5))

for i in range(5):
    plt.subplot(2,3,i+1)
    plt.imshow(imgs[i], 'gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()