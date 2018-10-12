import cv2

img = cv2.imread('./res/aero3.jpg')
print("pixel (150, 120) G value", img.item(150, 120, 0))

print("shape : ", img.shape)
print("size : ", img.size)
print("dtype : ", img.dtype)

img.itemset((150, 120, 0), 255)
print("pixel (150, 120) G value", img.item(150, 120, 0))

my_roi = img[0:100, 0:100]
img[300:400, 300:400] = my_roi

cv2.imwrite('./out/aer.jpg', img)
