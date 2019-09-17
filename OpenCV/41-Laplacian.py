import cv2 as cv
import numpy as np

fileList = ['res/mohu.jpg', 'res/mohu1.jpg', 'res/mohu2.jpg',
            'res/mohu3.png', 'res/mediablur.png', 'res/jeep.jpeg']

for f in fileList:
    imag = cv.imread(f)
    grayImag = cv.cvtColor(imag, cv.COLOR_BGR2GRAY)
    #grayImag = cv.GaussianBlur(grayImag, (3, 3), 0)
    canny = cv.Canny(grayImag, 200, 200)
    value = canny.var()
    print('Canny : ' + str(value))

    lapla = cv.Laplacian(grayImag, cv.CV_8U)
    imageVar = lapla.var()
    print('Laplacian : ' + str(imageVar))

    grayImag = cv.cvtColor(grayImag, cv.COLOR_GRAY2BGR)
    canny = cv.cvtColor(canny, cv.COLOR_GRAY2BGR)
    cv.putText(canny, str(int(value)), (0, 40), cv.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2)

    lapla = cv.cvtColor(lapla, cv.COLOR_GRAY2BGR)
    cv.putText(lapla, str(int(imageVar)), (0, 40), cv.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2)

    longimag = np.hstack((imag, canny, lapla))
    cv.namedWindow(f, 0)
    cv.imshow(f, longimag)

while(1):
    if(cv.waitKey(100)==27):
        break