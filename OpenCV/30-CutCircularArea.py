import cv2
import numpy as np

#加载图片
img = cv2.imread('./res/icon.png', cv2.IMREAD_UNCHANGED)

#获取图片尺寸
height, width = img.shape[:2]
height = int(height)
width = int(width)

#生成内显示模板
circleIn = np.zeros((height, width, 1), np.uint8)
circleIn = cv2.circle(circleIn, (width // 2, height // 2), min(height, width) // 2, (1), -1)
#实际使用中不需要写入文件
#np.savetxt('./out/circle.txt', circleIn[:, :, 0], fmt="%d", delimiter="")

#生成外显示模板
circleOut = circleIn.copy()
circleOut[circleOut == 0] = 2
circleOut[circleOut == 1] = 0
circleOut[circleOut == 2] = 1
#实际使用中不需要写入文件
#np.savetxt('./out/circle1.txt', circleOut[:, :, 0], fmt="%d", delimiter="")

#原图与内显示模板融合
#生成空白图片
imgIn = np.zeros((height, width, 4), np.uint8)
#复制前3个通道
imgIn[:, :, 0] = np.multiply(img[:, :, 0], circleIn[:, :, 0])
imgIn[:, :, 1] = np.multiply(img[:, :, 1], circleIn[:, :, 0])
imgIn[:, :, 2] = np.multiply(img[:, :, 2], circleIn[:, :, 0])
#设置α通道的不透明部分
circleIn[circleIn == 1] = 255
imgIn[:, :, 3] = circleIn[:, :, 0]
cv2.imwrite('./out/imgIn.png', imgIn)

#外显示与内显示同理
imgOut = np.zeros((height, width, 4), np.uint8)
imgOut[:, :, 0] = np.multiply(img[:, :, 0], circleOut[:, :, 0])
imgOut[:, :, 1] = np.multiply(img[:, :, 1], circleOut[:, :, 0])
imgOut[:, :, 2] = np.multiply(img[:, :, 2], circleOut[:, :, 0])
circleOut[circleOut == 1] = 255
imgOut[:, :, 3] = circleOut[:, :, 0]
cv2.imwrite('./out/imgOut.png', imgOut)