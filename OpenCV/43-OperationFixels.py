import cv2 as cv
import numpy as np

img_down = cv.imread('./res/underexposed.jpg')
img_up = cv.imread('./res/Overexposed.jpg')

cv.imshow('Down', img_down)
cv.imshow('Up', img_up)

H, W = img_down.shape[:2]
print(H, W)
filter_up = np.ones_like(img_down)
filter_down = np.ones_like(img_up)

clip_h = int(H/3)
clip_w = int(W/3)

#进行相加操作
filter_up[clip_h:clip_h * 2, clip_w:clip_w * 2, :] = 100
img_add = cv.add(img_down, filter_up)# same  img + filt
cv.imshow('add', img_add)

#进行相乘操作
filter_up[clip_h:clip_h * 2, clip_w:clip_w * 2, :] = 3
img_mult = cv.multiply(img_down, filter_up) #same img * filt
cv.imshow('multiply', img_mult)

#进行减法操作
filter_down[clip_h:clip_h * 2, clip_w:clip_w * 2, :] = 100
img_sub = cv.subtract(img_up, filter_down) #same img - filt
cv.imshow('subtract', img_sub)

#进行除法操作
filter_down[clip_h:clip_h * 2, clip_w:clip_w * 2, :] = 2.5
img_divi = cv.divide(img_up, filter_down)
cv.imshow('divide', img_divi)

#两个图片进行融合处理
img_up = cv.resize(img_up, (W, H), interpolation=cv.INTER_CUBIC)
img_merge = img_up - img_down
img_merge[img_merge > img_up] = 0
cv.imshow('merge', img_merge)

while True:
    key = cv.waitKey(100)
    if key == 27:
        break
cv.destroyAllWindows()