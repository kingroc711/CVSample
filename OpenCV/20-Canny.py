import cv2
from matplotlib import pyplot as plt

img = cv2.imread('./res/mini.jpeg',0)
edges = cv2.Canny(img,150,200)
plt.figure(figsize = (20, 10))

plt.subplot(1, 2, 1)
plt.imshow(img,cmap = 'gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image')
plt.axis('off')

plt.show()