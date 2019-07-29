import cv2
import numpy as np
from matplotlib import pyplot as plt


def main():
    Overexpose = cv2.imread("res/Overexposed.jpg")
    underexpose = cv2.imread("res/underexposed.jpg")
    #cv2.imshow("Over", Overexpose)
    #cv2.imshow("under", underexpose)
    plt.figure(1)

    plt.subplot(4,2,1)
    plt.imshow(Overexpose)

    plt.subplot(4,2,2)
    plt.imshow(underexpose)

    plt.subplot(4, 2, 3)
    chans = cv2.split(Overexpose)
    colors = ("b", "g", "r")
    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])

    plt.subplot(4, 2, 4)
    chans = cv2.split(underexpose)
    colors = ("b", "g", "r")
    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])

    plt.subplot(4, 2, 5)
    equalizeOver = np.zeros(Overexpose.shape, Overexpose.dtype)
    equalizeOver[:, :, 0] = cv2.equalizeHist(Overexpose[:, :, 0])
    equalizeOver[:, :, 1] = cv2.equalizeHist(Overexpose[:, :, 1])
    equalizeOver[:, :, 2] = cv2.equalizeHist(Overexpose[:, :, 2])
    plt.imshow(equalizeOver)
    cv2.imwrite('./out/equlizeOver.jpg', equalizeOver)
#    cv2.imshow('equalizeOver', equalizeOver)

    plt.subplot(4, 2, 6)
    equalizeUnder = np.zeros(underexpose.shape, underexpose.dtype)
    equalizeUnder[:, :, 0] = cv2.equalizeHist(underexpose[:, :, 0])
    equalizeUnder[:, :, 1] = cv2.equalizeHist(underexpose[:, :, 1])
    equalizeUnder[:, :, 2] = cv2.equalizeHist(underexpose[:, :, 2])
    plt.imshow(equalizeUnder)
    cv2.imwrite('./out/equalizeunder.jpg', equalizeUnder)

    plt.subplot(4, 2, 7)
    chans = cv2.split(equalizeOver)
    colors = ("b", "g", "r")
    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])

    plt.subplot(4, 2, 8)
    chans = cv2.split(equalizeUnder)
    colors = ("b", "g", "r")
    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])

    plt.show()
    cv2.waitKey(0)

if __name__ == '__main__':
    main()