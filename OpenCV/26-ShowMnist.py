from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import cv2

mnist = input_data.read_data_sets("MNIST_data", one_hot=True)

images = []
img = []

for i in range(mnist.train.images.shape[0]):
    im = mnist.train.images[i]
    im = im.reshape(28, 28)
    if(img == []):
        img = im
    else :
        #横向组合
        img = np.hstack((img, im))

    #每行显示60个数字图片
    if (img.shape[1] / 28 == 60):
        if(images == []):
            images = img.copy()
            img = []
        else:
            #纵向组合
            images = np.vstack((images, img))
            img = []

    if(i == 1200):
        break;

cv2.imshow('reSize2', images)
cv2.waitKey()
cv2.destroyAllWindows()
