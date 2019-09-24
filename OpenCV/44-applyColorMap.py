import cv2 as cv

gray = cv.imread('./res/habo.jpeg')
#cv.imshow('gray', gray)

g_autumn = cv.applyColorMap(gray,  cv.COLORMAP_TURBO)
cv.imshow('g_autumn', g_autumn)

while True:
    if cv.waitKey(100) == 27:
        break
cv.destroyAllWindows()


